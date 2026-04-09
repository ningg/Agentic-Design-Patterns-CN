# Publish as Website (MkDocs)

Use the following commands in the repository root to preview this `cn` directory as a website:

```bash
python -m pip install -r requirements-docs.txt
python scripts/generate_mkdocs_nav.py
mkdocs serve
```

Build static files:

```bash
mkdocs build --strict
```

This repository includes `.github/workflows/deploy-docs.yml`, which deploys the site to GitHub Pages on every push to `main`.

> 发布为网站（MkDocs）
>
> 在仓库根目录执行以下命令，可将 `cn` 目录预览为文档网站：
>
> ```bash
> python -m pip install -r requirements-docs.txt
> python scripts/generate_mkdocs_nav.py
> mkdocs serve
> ```
>
> 构建静态站点：
>
> ```bash
> mkdocs build --strict
> ```
>
> 仓库已包含 `.github/workflows/deploy-docs.yml`，推送到 `main` 分支后会自动发布到 GitHub Pages。
