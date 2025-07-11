import os
import re
import shutil

# Your paths
vault_root = r"C:\Users\abhir\OneDrive\Documents\Obsidian Vault"
vault_post_dir = os.path.join(vault_root, "post")
static_images_dir = r"C:\Users\abhir\abhi-blog\static\images"

# Loop through .md files in post
for filename in os.listdir(vault_post_dir):
    if filename.endswith(".md"):
        md_path = os.path.join(vault_post_dir, filename)
        with open(md_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Match Obsidian-style image syntax
        matches = re.findall(r'!\[\[(Pasted image[^\]]+\.png)\]\]', content)
        for img_name in matches:
            full_img_path = os.path.join(vault_root, img_name)
            if os.path.exists(full_img_path):
                shutil.copy2(full_img_path, static_images_dir)

            # Convert to Hugo markdown
            hugo_md = f"![{img_name}](/images/{img_name.replace(' ', '%20')})"
            content = content.replace(f"![[{img_name}]]", hugo_md)

        # Save modified content
        with open(md_path, "w", encoding="utf-8") as file:
            file.write(content)

print("✅ Obsidian image syntax fixed & images copied.")
