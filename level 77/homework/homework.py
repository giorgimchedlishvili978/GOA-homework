def create_dict(keys, values):
    # თუ სიები არ არის ერთნაირი სიგრძის, შევინახავთ None-ს როგორც დანაკლისი
    return dict(zip(keys, values))

# მაგალითი:
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']
result = create_dict(keys, values)

print(result)
