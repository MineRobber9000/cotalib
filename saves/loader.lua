lume = require "lume"
json = require "json"

local file = ...
local handle = io.open(file,"r")
local text = handle:read("*a")
local tbl = lume.deserialize(text)
print(json.encode(tbl))
