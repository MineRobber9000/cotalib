from libsave import Save

with open("examplesave.json") as f:
	example = f.read().strip()

#print("BASE SAVE")
test = Save.from_json(example)
print(",".join(test.data.keys()))

with open("examplerec.save","w") as f:
	f.write(test.lua)
