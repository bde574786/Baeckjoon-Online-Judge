import sys

input = sys.stdin.readline
n, m = map(int, input().strip().split())

password_dict = {}
for i in range(n):
    site, password = input().strip().split()
    password_dict[site] =  password
    
sites = []
for i in range(m):
    site = input().strip()
    sites.append(site)
    
for site in sites:
    print(password_dict[site])
