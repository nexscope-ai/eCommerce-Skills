# Repository Setup Guide

## Repository Information

**Name**: `ecommerce-skills`
**Description**: `Cross-platform e-commerce skills for OpenClaw — Shopify, Etsy, WooCommerce, and universal tools for online sellers`
**Topics/Tags**: `ecommerce`, `openclaw`, `skills`, `shopify`, `etsy`, `ai-tools`, `marketing`, `seo`, `dropshipping`
**License**: MIT

## GitHub Settings

### Basic Info
- **Homepage URL**: `https://nexscope.ai` 
- **Repository name**: `ecommerce-skills`
- **Description**: Cross-platform e-commerce skills for OpenClaw — Shopify, Etsy, WooCommerce, and universal tools for online sellers
- **Public repository**: ✅ Yes
- **Initialize with README**: ❌ No (we'll push our own)

### Repository Topics
Add these topics for discoverability:
```
ecommerce, openclaw, skills, ai-tools, shopify, etsy, woocommerce, 
marketing, seo, dropshipping, automation, business-tools
```

### Branch Protection
- Default branch: `main`
- Consider protecting `main` branch once you have collaborators

## Token Permissions Needed

The Personal Access Token needs these scopes:
- ✅ `repo` (Full control of private repositories)
- ✅ `workflow` (Update GitHub Action workflows) 
- ✅ `write:packages` (Upload packages to GitHub Package Registry)
- ✅ `read:org` (Read org and team membership, read org projects)

## Initial Push Commands

After creating the repository, you'll run:

```bash
git clone https://github.com/nexscope-ai/ecommerce-skills.git
cd ecommerce-skills

# Copy our prepared files
cp -r /root/.openclaw/workspace2/ecommerce-skills-repo-content/* .

# Initial commit
git add .
git commit -m "Initial repository setup

- Cross-platform e-commerce skills for OpenClaw
- 41 planned skills across 9 categories  
- Covers Shopify, Etsy, WooCommerce, and universal tools
- Built by Nexscope for the e-commerce community"

git push origin main
```

## Organization Profile

Make sure the `nexscope-ai` organization has:
- Profile picture/avatar
- Organization description mentioning e-commerce AI tools
- Website link to nexscope.ai
- Public visibility for repositories

This will be a public showcase repository, so presentation matters!