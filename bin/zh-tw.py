#!/usr/bin/env python3
import os, sys, opencc

def convert(src_path, dst_path, cfg='s2twp.json'):
    converter = opencc.OpenCC(cfg)
    with open(src_path, "r", encoding='utf-8') as src, open(dst_path, "w+", encoding='utf-8') as dst:
        dst.write("\n".join(
            converter.convert(line.rstrip()).replace('(img/', '(../img/')
                .replace('髮送', '傳送')
                .replace('髮布', '釋出')
                .replace('髮生', '發生')
                .replace('髮出', '發出')
                for line in src))
    print(f"convert {src_path} to {dst_path}")


if __name__ == '__main__':
    print(sys.argv)
    home = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), '..'))
    os.chdir(home)
    for f in os.listdir():
        if f.endswith('.md'):
            convert(f, f"zh-tw/{f}")
