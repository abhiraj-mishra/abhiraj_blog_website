# Set paths
$sourcePath = "C:\Users\abhir\OneDrive\Documents\Obsidian Vault\post"
$destinationPath = "C:\Users\abhir\abhi-blog\content\posts"
$myrepo = "git@github.com:abhiraj-mishra/abhiraj_blog_website.git"

# Setup
$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $ScriptDir

# Command checks
$requiredCommands = @('git', 'hugo')
$pythonCommand = if (Get-Command 'python' -ErrorAction SilentlyContinue) { 'python' } elseif (Get-Command 'python3' -ErrorAction SilentlyContinue) { 'python3' } else { Write-Error "Python not found."; exit 1 }

foreach ($cmd in $requiredCommands) {
    if (-not (Get-Command $cmd -ErrorAction SilentlyContinue)) {
        Write-Error "$cmd is not in PATH."
        exit 1
    }
}

# Git setup
if (-not (Test-Path ".git")) {
    git init
    git remote add origin $myrepo
} elseif (-not ((git remote) -contains "origin")) {
    git remote add origin $myrepo
}

# Sync Obsidian to Hugo
Write-Host "`n📦 Syncing posts from Obsidian..."
robocopy $sourcePath $destinationPath /MIR /Z /W:5 /R:3
if ($LASTEXITCODE -ge 8) {
    Write-Error "Robocopy failed."
    exit 1
}

# Fix image syntax
Write-Host "`n🖼️ Fixing image links..."
if (-not (Test-Path "images.py")) {
    Write-Error "images.py not found!"
    exit 1
}
& $pythonCommand images.py

# Build Hugo site
Write-Host "`n⚙️ Building Hugo site..."
hugo

# Git Add + Commit
Write-Host "`n🔧 Staging changes..."
if ((git status --porcelain) -ne "") {
    git add .
    $msg = "New Blog Post on $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
    git commit -m $msg
}

# Push to master
Write-Host "`n🚀 Pushing to master..."
git push origin master

# Deploy to Hostinger
Write-Host "`n🌍 Deploying to Hostinger branch..."
if (git branch --list "hostinger-deploy") {
    git branch -D hostinger-deploy
}
git subtree split --prefix public -b hostinger-deploy
git push origin hostinger-deploy:hostinger --force
git branch -D hostinger-deploy

Write-Host "`n✅ All done!"
