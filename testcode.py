class Pokemon:

    def __init__(self, NAME,HP, A ,B ,C,D,S):
        self.NAME = NAME
        self.HP = HP
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.S = S

    def damageCalc(self):
        damage = self.A * 100
        return damage


brimon = Pokemon("ブリムオン",57,90,95,136,103,29)

dorapurt = Pokemon("ドラパルト",88,120,75,100,75,142)

print(brimon.NAME)
print(brimon.HP)
print(brimon.A)
print(brimon.B)
print(brimon.C)
print(brimon.D)
print(brimon.S)

brimon_damage = brimon.damageCalc()
dorapurt_damage = dorapurt.damageCalc()

print("??????????????????????????????????????????")

print("ブリムオンのダメージ：", brimon_damage)
print("ドラパルトのダメージ：", dorapurt_damage)