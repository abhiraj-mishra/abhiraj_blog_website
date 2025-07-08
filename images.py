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

















# import os
# import re
# import shutil

# # Paths (using raw strings to handle Windows backslashes correctly)
# posts_dir = r"C:\Users\abhir\OneDrive\Documents\Obsidian Vault\blog"
# attachments_dir = r"C:\Users\abhir\OneDrive\Documents\Obsidian Vault"
# static_images_dir = r"C:\Users\abhir\abhi-blog\static\images"

# # Step 1: Process each markdown file in the posts directory
# for filename in os.listdir(posts_dir):
#     if filename.endswith(".md"):
#         filepath = os.path.join(posts_dir, filename)
        
#         with open(filepath, "r", encoding="utf-8") as file:
#             content = file.read()
        
#         # Step 2: Find all image links in the format ![Image Description](/images/Pasted%20image%20...%20.png)
#         images = re.findall(r'\[\[([^]]*\.png)\]\]', content)
        
#         # Step 3: Replace image links and ensure URLs are correctly formatted
#         for image in images:
#             # Prepare the Markdown-compatible link with %20 replacing spaces
#             markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
#             content = content.replace(f"[[{image}]]", markdown_image)
            
#             # Step 4: Copy the image to the Hugo static/images directory if it exists
#             image_source = os.path.join(attachments_dir, image)
#             if os.path.exists(image_source):
#                 shutil.copy(image_source, static_images_dir)

#         # Step 5: Write the updated content back to the markdown file
#         with open(filepath, "w", encoding="utf-8") as file:
#             file.write(content)

# print("Markdown files processed and images copied successfully.")
