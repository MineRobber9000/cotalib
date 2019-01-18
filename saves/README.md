# cotalib/saves

Programs for save export, import and modification.

## Files

 - `libsave.py` *(lib)* - Includes a save loading library with exports (currently only to JSON).
 - `*.lua` - any .lua files are needed to ease issues with parsing lume.lua serialized tables.
 - `savetojson.py` - currently outputs all available savefile keys and converts `examplelua.save` to `examplesave.json`

## Explanation

Curse of the Arrow saves its state in a file located at `path/to/love/data/CurseOfTheArrow/curse_of_the_arrow.save`. Anything that needs to be persisted is stored in this file.

rxi's LUME library is used to serialize the data. `loader.lua` simply deserializes the save and then, using rxi's json.lua library, outputs the deserialized table as JSON.

libsave simply reads this and moves some keys around. All of the data remains as in the original save.

When lua export is implemented, it will load the JSON and turn it back into lua (using `dumper.lua` or a similarly named helper).

