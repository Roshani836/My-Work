scores=["75","32","88","42"]
for score in scores:
    if int(score) >= 40:
        print(f"Pass with " , score)
    else:
        print(f"Fail with " , score)