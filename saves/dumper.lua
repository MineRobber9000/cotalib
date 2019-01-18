lume = require "lume"
json = require "json"

local file = ...
local handle = io.open(file,"r")
local text = handle:read("*a")
local tbl = json.decode(text)
print(lume.serialize(tbl))
