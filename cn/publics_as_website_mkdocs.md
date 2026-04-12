# Publish as Website (MkDocs)

This repository uses `mkdocs` + `mkdocs-material` + `mkdocs-with-pdf`.

The MkDocs config is in `mkdocs.yml`, and the PDF plugin writes to:

```text
site/pdf/Agentic-Design-Patterns-CN.pdf
```

## PDF plugin switch (`MKDOCS_ENABLE_PDF`)

`mkdocs.yml` sets `enabled_if_env: MKDOCS_ENABLE_PDF`. The PDF plugin only runs when this variable is `1`, but MkDocs still imports the plugin during config loading. Therefore the strict CI check uses a separate `mkdocs-strict.yml` file that omits `with-pdf` entirely:

- **`MKDOCS_ENABLE_PDF` unset or `0`**: skips PDF rendering (faster; no WeasyPrint layout pass). You can run `mkdocs build --strict` without `mkdocs-with-pdf` counting WeasyPrint log lines as build failures. (The package still imports WeasyPrint; on macOS you still need native libraries as in §3.2.)
- **`MKDOCS_ENABLE_PDF=1`**: builds `site/pdf/Agentic-Design-Patterns-CN.pdf`. Do **not** use `mkdocs build --strict` here: in strict mode, `mkdocs-with-pdf` counts WeasyPrint log lines as fatal errors, and Material’s CSS triggers thousands of them even when the PDF file is produced.

GitHub Actions runs a strict build with `mkdocs-strict.yml`, then a second build with PDF enabled and `--no-strict`.

## 1. Preview the website locally

From the repository root, run:

```bash
bash scripts/docs-serve.sh
```

The script will:

- create or reuse the local `.venv`
- install `requirements-docs.txt`
- regenerate MkDocs navigation
- start `mkdocs serve` with `mkdocs-strict.yml` for hot reload without loading the PDF plugin

Default address:

```text
http://127.0.0.1:8000/Agentic-Design-Patterns-CN/
```

Optional: override the bind address or port:

```bash
MKDOCS_DEV_ADDR=0.0.0.0:8001 bash scripts/docs-serve.sh
```

## 2. Build the static website

```bash
python3 scripts/generate_mkdocs_nav.py
# Strict check, HTML only (no PDF plugin loaded)
python3 -m mkdocs build --strict -f mkdocs-strict.yml

# Full site including PDF (omit --strict; see “PDF plugin switch” above)
MKDOCS_ENABLE_PDF=1 python3 -m mkdocs build
```

## 3. Export PDF on macOS

On this machine, the most stable approach is to use a repository-local virtual environment created from the local Anaconda Python.

### 3.1 Create the docs virtual environment

```bash
/Users/guoning/anaconda3/bin/python3 -m venv .venv-docs
./.venv-docs/bin/python -m pip install --upgrade pip
./.venv-docs/bin/pip install -r requirements-docs.txt
python3 scripts/generate_mkdocs_nav.py
```

### 3.2 If WeasyPrint cannot load native libraries

If `mkdocs build` fails with errors like `cannot load library 'libgobject-2.0-0'` or `cannot load library 'libpango-1.0-0'`, create compatibility symlinks from Homebrew libraries into the Anaconda `lib` directory:

```bash
ln -sf /opt/homebrew/lib/libgobject-2.0.dylib /Users/guoning/anaconda3/lib/libgobject-2.0-0
ln -sf /opt/homebrew/lib/libglib-2.0.dylib /Users/guoning/anaconda3/lib/libglib-2.0-0
ln -sf /opt/homebrew/lib/libpango-1.0.dylib /Users/guoning/anaconda3/lib/libpango-1.0-0
ln -sf /opt/homebrew/lib/libpangocairo-1.0.dylib /Users/guoning/anaconda3/lib/libpangocairo-1.0-0
ln -sf /opt/homebrew/lib/libpangoft2-1.0.dylib /Users/guoning/anaconda3/lib/libpangoft2-1.0-0
```

### 3.3 Build the site and export PDF

```bash
DYLD_FALLBACK_LIBRARY_PATH="/Users/guoning/anaconda3/lib:/opt/homebrew/lib:$DYLD_FALLBACK_LIBRARY_PATH" \
MKDOCS_ENABLE_PDF=1 ./.venv-docs/bin/python -m mkdocs build
```

Generated file:

```text
site/pdf/Agentic-Design-Patterns-CN.pdf
```

## 4. Verify the exported PDF

Check the output file:

```bash
ls -lh site/pdf/Agentic-Design-Patterns-CN.pdf
```

Optional: verify that later chapters are really included:

```bash
python3 - <<'PY'
import fitz
doc = fitz.open("site/pdf/Agentic-Design-Patterns-CN.pdf")
toc = doc.get_toc(simple=True)
checks = ["Chapter 18", "Chapter 19", "Chapter 20", "Chapter 21", "Appendix G", "Glossary", "Conclusion"]
print("pages =", doc.page_count)
for item in checks:
    print(item, any(item in entry[1] for entry in toc))
PY
```

## 5. Known issue: PDF stops at Chapter 17

During PDF export on macOS, the build may appear to succeed, but the generated PDF can stop at `Chapter 17` and omit all later chapters.

The root cause found in this repository was the image:

```text
cn/assets-new/Example_of_DeepSearch_with_multiple_Reflection_Steps.png
```

When that image remained at its original size, `mkdocs-with-pdf` / `WeasyPrint` truncated the PDF after the final section of `Chapter 17`.

The working fix was to downscale that image before rebuilding the PDF.

Current working size:

```text
575 x 884
```

The image was originally:

```text
959 x 1474
```

If the truncation issue appears again after replacing that image, resize it to roughly `60%` of the original dimensions and rebuild:

```bash
python3 - <<'PY'
from PIL import Image
from pathlib import Path

path = Path("cn/assets-new/Example_of_DeepSearch_with_multiple_Reflection_Steps.png")
img = Image.open(path).convert("RGB")
w, h = img.size
resized = img.resize((int(w * 0.6), int(h * 0.6)), Image.LANCZOS)
resized.save(path, format="PNG", optimize=True)
print("old =", (w, h))
print("new =", resized.size)
PY
```

Then rerun:

```bash
DYLD_FALLBACK_LIBRARY_PATH="/Users/guoning/anaconda3/lib:/opt/homebrew/lib:$DYLD_FALLBACK_LIBRARY_PATH" \
MKDOCS_ENABLE_PDF=1 ./.venv-docs/bin/python -m mkdocs build
```

This repository includes `.github/workflows/deploy-docs.yml`, which deploys the site to GitHub Pages on every push to `main`.

> 发布为网站（MkDocs）
>
> 当前仓库使用 `mkdocs` + `mkdocs-material` + `mkdocs-with-pdf`。
>
> `mkdocs.yml` 中已启用 PDF 插件，默认输出路径为：
>
> ```text
> site/pdf/Agentic-Design-Patterns-CN.pdf
> ```
>
> ## PDF 插件开关（`MKDOCS_ENABLE_PDF`）
>
> `mkdocs.yml` 中配置了 `enabled_if_env: MKDOCS_ENABLE_PDF`，仅当该环境变量为 `1` 时才生成 PDF：
>
> - **未设置或为 `0`**：不执行 PDF 排版导出（更快；也不会把 WeasyPrint 日志当成构建失败）。可用 `mkdocs build --strict` 做 MkDocs 严格检查。（插件仍会 import WeasyPrint；macOS 上仍需 §3.2 的本机库。）
> - **`MKDOCS_ENABLE_PDF=1`**：生成 `site/pdf/Agentic-Design-Patterns-CN.pdf`。请勿与 `mkdocs build --strict` 同时使用：严格模式下 `mkdocs-with-pdf` 会把 WeasyPrint 的日志计为致命错误，Material 主题的 CSS 会产生数千条。
>
> GitHub Actions 会先做一次关闭 PDF 的 `--strict` 构建，再单独做一次带 PDF 且 `--no-strict` 的构建。
>
> ## 1. 本地预览网站
>
> 在仓库根目录执行：
>
> ```bash
> bash scripts/docs-serve.sh
> ```
>
> 该脚本会自动：
>
> - 创建或复用本地 `.venv`
> - 安装 `requirements-docs.txt`
> - 重新生成 MkDocs 导航
> - 使用 `mkdocs-strict.yml` 启动热更新预览，避免加载 PDF 插件
>
> 默认访问地址：
>
> ```text
> http://127.0.0.1:8000/Agentic-Design-Patterns-CN/
> ```
>
> 如需自定义监听地址或端口，可执行：
>
> ```bash
> MKDOCS_DEV_ADDR=0.0.0.0:8001 bash scripts/docs-serve.sh
> ```
>
> ## 2. 构建静态网站
>
> ```bash
> python3 scripts/generate_mkdocs_nav.py
> MKDOCS_ENABLE_PDF=0 python3 -m mkdocs build --strict
> MKDOCS_ENABLE_PDF=1 python3 -m mkdocs build
> ```
>
> ## 3. 在 macOS 上导出 PDF
>
> 在当前机器上，最稳妥的方式是使用仓库内独立虚拟环境 `.venv-docs`，并基于本机 Anaconda Python 创建。
>
> ### 3.1 创建文档环境
>
> ```bash
> /Users/guoning/anaconda3/bin/python3 -m venv .venv-docs
> ./.venv-docs/bin/python -m pip install --upgrade pip
> ./.venv-docs/bin/pip install -r requirements-docs.txt
> python3 scripts/generate_mkdocs_nav.py
> ```
>
> ### 3.2 如果 WeasyPrint 缺少本机动态库
>
> 若遇到 `cannot load library 'libgobject-2.0-0'`、`cannot load library 'libpango-1.0-0'` 之类报错，可先将 Homebrew 的动态库链接到 Anaconda 的 `lib` 目录：
>
> ```bash
> ln -sf /opt/homebrew/lib/libgobject-2.0.dylib /Users/guoning/anaconda3/lib/libgobject-2.0-0
> ln -sf /opt/homebrew/lib/libglib-2.0.dylib /Users/guoning/anaconda3/lib/libglib-2.0-0
> ln -sf /opt/homebrew/lib/libpango-1.0.dylib /Users/guoning/anaconda3/lib/libpango-1.0-0
> ln -sf /opt/homebrew/lib/libpangocairo-1.0.dylib /Users/guoning/anaconda3/lib/libpangocairo-1.0-0
> ln -sf /opt/homebrew/lib/libpangoft2-1.0.dylib /Users/guoning/anaconda3/lib/libpangoft2-1.0-0
> ```
>
> ### 3.3 构建站点并导出 PDF
>
> ```bash
> DYLD_FALLBACK_LIBRARY_PATH="/Users/guoning/anaconda3/lib:/opt/homebrew/lib:$DYLD_FALLBACK_LIBRARY_PATH" \
> MKDOCS_ENABLE_PDF=1 ./.venv-docs/bin/python -m mkdocs build
> ```
>
> 输出文件：
>
> ```text
> site/pdf/Agentic-Design-Patterns-CN.pdf
> ```
>
> ## 4. 验证 PDF 是否完整
>
> 查看文件是否生成：
>
> ```bash
> ls -lh site/pdf/Agentic-Design-Patterns-CN.pdf
> ```
>
> 如需确认后续章节确实已进入 PDF，可执行：
>
> ```bash
> python3 - <<'PY'
> import fitz
> doc = fitz.open("site/pdf/Agentic-Design-Patterns-CN.pdf")
> toc = doc.get_toc(simple=True)
> checks = ["Chapter 18", "Chapter 19", "Chapter 20", "Chapter 21", "Appendix G", "Glossary", "Conclusion"]
> print("pages =", doc.page_count)
> for item in checks:
>     print(item, any(item in entry[1] for entry in toc))
> PY
> ```
>
> ## 5. 已知问题：PDF 在 Chapter 17 截断
>
> 在当前仓库中，曾出现 `mkdocs build` 表面成功，但导出的 PDF 只到 `Chapter 17`、后续章节全部缺失的问题。
>
> 根因定位到这张图片：
>
> ```text
> cn/assets-new/Example_of_DeepSearch_with_multiple_Reflection_Steps.png
> ```
>
> 当它保持原始尺寸时，`mkdocs-with-pdf` / `WeasyPrint` 会在 `Chapter 17` 最后一个小节之后截断 PDF。
>
> 可行修复方式是：先将这张图缩小，再重新构建 PDF。
>
> 当前可工作的尺寸是：
>
> ```text
> 575 x 884
> ```
>
> 原始尺寸是：
>
> ```text
> 959 x 1474
> ```
>
> 如果未来替换该图后问题再次出现，可按约 `60%` 比例重新导出：
>
> ```bash
> python3 - <<'PY'
> from PIL import Image
> from pathlib import Path
>
> path = Path("cn/assets-new/Example_of_DeepSearch_with_multiple_Reflection_Steps.png")
> img = Image.open(path).convert("RGB")
> w, h = img.size
> resized = img.resize((int(w * 0.6), int(h * 0.6)), Image.LANCZOS)
> resized.save(path, format="PNG", optimize=True)
> print("old =", (w, h))
> print("new =", resized.size)
> PY
> ```
>
> 然后重新执行：
>
> ```bash
> DYLD_FALLBACK_LIBRARY_PATH="/Users/guoning/anaconda3/lib:/opt/homebrew/lib:$DYLD_FALLBACK_LIBRARY_PATH" \
> MKDOCS_ENABLE_PDF=1 ./.venv-docs/bin/python -m mkdocs build
> ```
>
> 仓库已包含 `.github/workflows/deploy-docs.yml`，推送到 `main` 分支后会自动发布到 GitHub Pages。

