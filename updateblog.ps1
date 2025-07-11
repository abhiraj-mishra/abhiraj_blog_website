robocopy "C:\Users\abhir\OneDrive\Documents\Obsidian Vault\post" "C:\Users\abhir\abhi-blog\content\posts" /mir

python images.py  

# Generate current date/time string
$datetime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
git add .
git commit -m "Update on $datetime"

hugo -D -t terminal

git remote -v

git push origin main
git pull origin main

echo "Deploying to GitHub Hostinger..."
git subtree split --prefix public -b hostinger-deploy
git push origin hostinger-deploy:hostinger --force
git branch -D hostinger-deploy

echo "Done. You can preview with:"
echo "hugo server -t terminal"

