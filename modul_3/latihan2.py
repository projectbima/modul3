def konversi_menit(minggu=0, hari=0, jam=0, menit=0):
    total_menit = ((minggu * 7 + hari) * 24 + jam) * 60 + menit
    return total_menit

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

OutputData = []

for item in data:
    components = item.split()
    numeric_values = list(filter(str.isdigit, components))
    OutputData.append(numeric_values)

for item in OutputData:
    print(item)
