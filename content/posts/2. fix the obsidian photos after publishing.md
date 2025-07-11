---
title: abhiraj-blog-2
date: 2025-07-08
draft: false
tags:
  - abhiraj06
  - blog
---
# once we published the blog the image changed their names like this ![Pasted image 20250708231636.png](/images/Pasted%20image%2020250708231636.png)

has been changed to
```
we are making this blogging journey possible besause of 
![Pasted image 20250708221818.png](/images/Pasted%20image%2020250708221818.png)
it is obsidian a note taker

and

![Pasted image 20250708221908.png](/images/Pasted%20image%2020250708221908.png)
Hugo is one of the most popular open-source project. With its amazing speed and flexibility, Hugo makes building websites fun again.



!![Image](/images/Pasted%20image%2020250708220245.png)
an example 👍
```
by a python scrip 

```
import os

import re

  

# Path to folder with Markdown files

folder_path = r"C:\Users\path\to\Obsidian Vault\post"

  

# Regex to match the full Markdown image syntax with Pasted image pattern

pattern = re.compile(r'!\[Pasted image (\d+\.png)\]\(/images/Pasted%20image%20\d+\.png\)')

  

# Go through each .md file in the folder

for filename in os.listdir(folder_path):

    if filename.endswith(".md"):

        filepath = os.path.join(folder_path, filename)

  

        with open(filepath, "r", encoding="utf-8") as f:

            content = f.read()

  

        # Replace with Obsidian-style embed

        new_content = pattern.sub(r'![[Pasted image \1]]', content)

  

        if new_content != content:

            with open(filepath, "w", encoding="utf-8") as f:

                f.write(new_content)

            print(f"✅ Fixed: {filename}")
```

hope you like it
from next blog we will be dam serious