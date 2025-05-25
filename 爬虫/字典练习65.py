#字典里包含列表
# 嵌套列表的字典
company = {
    "name": "TechCorp",
    "departments": ["研发部", "市场部", "财务部"],
    "employee_ids": [1001, 1002, 1003]
}

# 混合类型字典
product = {
    "id": "P-001",
    "tags": ["电子产品", "热销", "蓝牙"],
    "prices": [299.99, 259.99]  # 价格历史记录
}

#从列表里拿出值
print(company["departments"][1])

print(product["id"])

print(product["prices"][0])
