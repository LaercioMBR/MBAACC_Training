from ctypes import create_string_buffer
Bar80_flag = 0
bar_range = 80


class Character_info:
    def __init__(self):
        self.dmp_ad = 0x00
        self.anten_stop_ad = 0x00
        self.anten_stop2_ad = 0x00
        self.atk_ad = 0x00
        self.gauge_ad = 0x00
        self.hit_ad = 0x00
        self.hitstop_ad = 0x00
        self.inv_ad = 0x00
        self.moon_ad = 0x00
        self.moon_st_ad = 0x00
        self.motion_ad = 0x00
        self.motion_type_ad = 0x00
        self.noguard_ad = 0x00
        self.seeld_ad = 0x00
        self.step_inv_ad = 0x00
        self.tag_flag_ad = 0x00
        self.ukemi1_ad = 0x00
        self.ukemi2_ad = 0x00
        self.x_ad = 0x00
        self.stop_ad = 0x00
        self.atk_st_ad_pointer_ad = 0x00
        self.atk_st_ad = 0x00
        self.throw_ad = 0x00




        self.b_dmp = create_string_buffer(971)
        self.b_anten_stop = create_string_buffer(1)
        self.b_anten_stop2 = create_string_buffer(4)
        self.b_atk = create_string_buffer(4)
        self.b_gauge = create_string_buffer(4)
        self.b_hit = create_string_buffer(2)
        self.b_hitstop = create_string_buffer(1)
        self.b_inv = create_string_buffer(1)
        self.b_moon = create_string_buffer(4)
        self.b_moon_st = create_string_buffer(1)
        self.b_motion = create_string_buffer(4)
        self.b_motion_type = create_string_buffer(2)
        self.b_noguard = create_string_buffer(1)
        self.b_seeld = create_string_buffer(1)
        self.b_step_inv = create_string_buffer(1)
        self.b_tag_flag = create_string_buffer(1)
        self.b_ukemi1 = create_string_buffer(2)
        self.b_ukemi2 = create_string_buffer(2)
        self.b_x = create_string_buffer(4)
        self.b_stop = create_string_buffer(1)

        self.b_atk_st_ad_pointer = create_string_buffer(4)
        self.b_atk_st = create_string_buffer(1)

        self.b_throw = create_string_buffer(4)


        self.anten_stop = 0
        self.anten_stop2 = 0
        self.anten_stop2_old = 0
        self.atk = 0
        self.gauge = 0
        self.hit = 0
        self.hitstop = 0
        self.hitstop_old = 0
        self.stop = 0
        self.inv = 0
        self.moon = 0
        self.moon_st = 0
        self.motion = 0
        self.motion_type = 0
        self.motion_type_old = 0
        self.motion_chenge_flag = 0
        self.noguard = 0
        self.seeld = 0
        self.step_inv = 0
        self.tag_flag = 0
        self.ukemi1 = 0
        self.ukemi2 = 0
        self.x = 0
        self.act = 0
        self.zen = 0
        self.act_flag = 0
        self.Bar_1 = ''
        self.Bar_2 = ''
        self.barlist_1 = list(range(bar_range))
        self.barlist_2 = list(range(bar_range))
        self.format = ''
        self.atk_st_ad_pointer = 0
        self.atk_st = 0
        self.throw = 0

P_info = [Character_info(), Character_info(), Character_info(), Character_info()]
p_info = [Character_info(), Character_info(), Character_info(), Character_info()]
for info1, info2 in zip(P_info, p_info):
    for n in range(bar_range):
        info1.barlist_1[n] = ""
        info2.barlist_1[n] = ""
        info1.barlist_2[n] = ""
        info2.barlist_2[n] = ""

P1 = P_info[0]
P2 = P_info[1]
P3 = P_info[2]
P4 = P_info[3]

p1 = p_info[0]
p2 = p_info[1]
p3 = p_info[2]
p4 = p_info[3]

st_barlist = list(range(bar_range))
for n in range(bar_range):
    st_barlist[n] = ""

b_cam = create_string_buffer(1500)
b_damage = create_string_buffer(4)
b_damage2 = create_string_buffer(4)

b_timer = create_string_buffer(4)

b_dmy_timer = create_string_buffer(4)
b_fn1_key = create_string_buffer(1)
b_fn2_key = create_string_buffer(1)
temp = create_string_buffer(4)
b_dummy_status = create_string_buffer(1)
b_game_mode = create_string_buffer(1)
b_obj = create_string_buffer(24)
b_recording_mode = create_string_buffer(1)
b_stop = create_string_buffer(2)

Bar_flag = 0
Bar_num = 0
DataFlag1 = 1
anten = 0
anten_flag = 0
bar_ini_flag = 0
bar_ini_flag2 = 0
base_ad = 0
damage = 0
debug_flag = 0
dummy_status = 0
f_timer = 0
f_timer2 = 0
fn1_key = 0
fn2_key = 0
h_pro = 0
hitstop = 0
hosei = 0
interval = 41
interval2 = 80
interval_time = 0
pid = 0
recording_mode = 0
reset_flag = 0
st_Bar = ""
stop = 0
ukemi = 0
ukemi2 = 0
advantage_f = 0
