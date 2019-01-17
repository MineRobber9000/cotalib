import subprocess, json, tempfile

class JSONImporter:
	@classmethod
	def _import(cls,data):
		return json.loads(data)

def parse_lua(data):
	tmp = tempfile.NamedTemporaryFile()
	with open(tmp.name,"w") as f:
		f.write(data)
	ret = subprocess.check_output(["/usr/bin/lua","loader.lua",tmp.name]).decode("ascii")
	tmp.close()
	return json.loads(ret)

class LuaImporter(JSONImporter):
	@classmethod
	def _import(cls,data):
		return parse_lua(data)

class Save:
	LUA_MAPPING = {"g_dif":"difficulty","g_shopped":"bought_items","g_index":"room_index","g_timer":"timer","g_bat":"flies_killed","g_et":"enable_timer_display","g_ess":"enable_screen_shake","g_es":"enable_sfx","g_money":"money","g_deaths":"death_count","g_game":"game","g_cubes":"cubes","g_ek":"on_screen_controls","g_played":"cutscene_played","g_ppet":"pet","g_ev":"enable_vibration","g_pix":"pixel_perfect","g_em":"enable_music"}
	def __init__(self,data,lua=False):
		self.data = data
		if lua:
			self.__migrate_from_lua__()
	def __migrate_from_lua__(self):
		odata = self.data
		self.data = {}
		for k in odata.keys():
			if k in self.LUA_MAPPING:
				self.data[self.LUA_MAPPING[k]]=odata[k]
			else:
				self.data[k]=odata[k]
	def __getitem__(self,k):
		return self.data[k]
	@property
	def json(self):
		return json.dumps(self.data)
	@property
	def lua(self):
		return "NYI"
	@classmethod
	def from_json(cls,data):
		return cls(JSONImporter._import(data))
	@classmethod
	def from_lua(cls,data):
		return cls(LuaImporter._import(data),True)
