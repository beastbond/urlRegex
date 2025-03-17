#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, pyperclip, webbrowser

urlRegex = re.compile(r'https?://[^\s,:);]+')

text = str(pyperclip.paste())

matches = []
for group in urlRegex.findall(text):
    matches.append(group)
# print(matches)
if len(matches) > 0:

    # pyperclip.copy('\n'.join(matches))   #debugging purposes obv
    # print('Copied back to clipboard')
    # print('\n'.join(matches))

    for link in matches:
        link = re.sub(r'[.;:]$', '', link) # Cleans up the link in case there is punctuation at the end
        webbrowser.open(link)

else:
    print("No matches were found")

