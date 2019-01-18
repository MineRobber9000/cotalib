from libsave import Save

with open("examplelua.save") as f:
	example = f.read().strip()

#print("BASE SAVE")
test = Save.from_lua(example)
print(",".join(test.data.keys()))

with open("examplesave.json","w") as f:
	f.write(test.json)
