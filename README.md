# Fame_and_Fortune
Fame & Fortune [RPG]

Stats:

Name	Category	Description 	Variable	Default 
Max HP	Health	Maximum value of HP	M	10
HP	Health	Health	H	{M}
HP Regen	Health	Amount of health regeneration per second	R	1
Max SP	Shield	Maximum value of shield 	N	0
SP	Shield	Bonus health (can be ignored)	S	{N}
SP Regen	Shield	Amount of shield regeneration per second	O	0
Damage	Battle	Damage dealt when attacking 	D	1
Atk Speed	Battle	Speed of attacks	C	1 sec
Armor	Battle	Amount of damage absorbed	A	10%
Critical Hit	Battle	Probability of attack being a critical hit	B	25%
Combo	Battle	Streak	Z	{0}
Accuracy	Battle 	Probability of attack landing	T	50%
Vulnerability	Battle 	Probability of getting hit	V	50%
Scavenge	Loot	Probability of finding items	I	50%
Rarity	Loot	Quality of items found	Q	0
Inventory Space	Loot	Max amount of items in inventory	Y	30
Buffs	Effects	All buffs	G	[]
Debuffs	Effects	All debuffs	F	[]
Effects Given	Effects	Effects given to enemies when attacked	K	[]
Medicine	Effects	Probability of getting buffs	P	20%
Sickness	Effects	Probability of getting debuffs	W	100%
Lvl	Level	Level	L	1
XP	Level	Points for levels	X	0
XP Earn	Level	Amount of XP per kill	E	5
Lvl Up	Level	Amount of XP needed to reach the next level	U	50
Rings	Character	Species and job	J	?


Variables:
First is self; second is enemy
Letter	Meaning
A-Z a-Z	Stats
Δ δ	Effect
Θ θ	Shield effectiveness 
Ω ω	Critical hit
α	Extra variable
Ψ ψ	Damage dealt
Γ γ	Rank of effect
Λ λ	Item
Φ φ	Rank of item
μ	Market Points
τ	Trait Points
ζ	Skill Points
υ	Upgrade Points
ν	Potion Points
ρ	Enemy’s Position
κ	Enemy’s Type
Ξ ξ	Item’s Quality
Π π	Item’s Type
β	Skill’s Level
ε	Skill
χ	Amount of furniture


Attack damage:

Hits = (t-V)%

If hits==1, continue; else, stop

Ω = B%

ψ = (d+10(z//5))*(Ω+1)*(100-A)%

If θ=0, skip until •; else, do not skip

α: lesser between S and ψ

S -= α

ψ -= α

•

α: lesser between H and ψ

H -= α

Z = 0

G +≈ k

F +≈ k

Effects:

Name	Buff/Debuff/Other	Effect	Duration 	Ranks	Probability	Opposite 	Abbreviation
Clear	Other	G = [] F = []	Ins	1-10	10Γ%	—	Clr
Cure	Other	F = []	Ins	1-10	10Γ%	Inf	Cur
Infect	Other	G = []	Ins	1-10	10Γ%	Cur	Inf
Amplify	Other	G!γ += Γ F!γ += Γ	Ins	1-3	30Γ%+5(P+W)%	Red	Amp
Reduce	Other	G!γ -= Γ F!γ -= Γ	Ins	1-3	30Γ%+5(P+W)%	Amp	Red
Heal	Buff	H += M*10Γ%	Ins	1-10	100%	Hurt	Hea
Hurt	Debuff	H -= M*10Γ%	Ins	1-10	100%	Heal	Hit
Regen	Buff	R *= (100+10Γ)%	5Γ sec	1-10	90%+10P%	Poison	Rgn
Poison 	Debuff	R *= -10Γ%	5Γ sec	1-10	90%+10W%	Regen	Poi
Protect	Buff	O *= (100+10Γ)%	5Γ sec	1-10	90%+10P%	Unprotect	Pro
Unprotect	Debuff	O *= (100-10Γ)%	5Γ sec	1-10	90%+10W%	Protect	Upr
Young	Buff	M *= (100+5Γ)%	10Γ sec	1-4	75%	Old	You
Old	Debuff	M *= (100-5Γ)%	10Γ sec	1-4	75%	Young	Old
Strength	Buff	D *= (100+10Γ)%	20Γ sec	1-10	80%+20P%	Weakness	Str
Weakness	Debuff	D *= (100-10Γ)%	20Γ sec	1-10	80%+20W%	Strength	Wea
Speed	Buff	C /= (100+25Γ)% V *= (100-25Γ)%	10Γ sec	1-4	85%+15P%	Slowness	Spe
Slowness	Debuff	C /= (100-25Γ)% V *= (100+25Γ)%	10Γ sec	1-4	85%+15W%	Speed	Slo
Sleep	Debuff	V *= 110% T = 0%	10Γ sec	1-6	90%+10W%	—	Zzz
Petrify	Debuff	C *= 200%	10Γ sec	1-6	80%+20W%	—	Pet
Lucky	Buff	E *= (100+5Γ)% I *= (100+10Γ)% Q *= (100+5Γ)% B = 100% P *= (100+5Γ)% W *= (100-5Γ)%	30Γ sec	1-4	90%+10P%	Unlucky	Lck
Unlucky	Debuff 	E *= (100-5Γ)% I *= (100-10Γ)% Q *= (100-5Γ)% B = 0% P *= (100-5Γ)% W *= (100+5Γ)%	30Γ sec	1-4	90%+10W%	Lucky	Ulk
Burn	Debuff 	C /= (90+5Γ)% R *= (100-5Γ)% T *= 90%	5Γ	1-3	90%	Freeze	Fir
Freeze	Debuff 	C /= (100-5Γ)% V *= (100+5Γ)% W *= (100+5Γ)%	5Γ	1-3	90%	Burn	Ice
Grow	Buff 	C /= (100/2^(Γ-1))% D *= (100+10Γ)% B = 100% A *= (100+10Γ)% T *= (100+10Γ)% V *= (100+10Γ)%	10Γ sec	1-4	75%+25P%-5W%	Shrink	Big
Shrink	Buff	C *= (100/2^(Γ-1))% D *= (100-10Γ)% B = 100% A *= (100-10Γ)% T *= (100-10Γ)% V *= (100-10Γ)%	10Γ sec	1-4	75%+25P%-5W%	Grow	Sma
Mirror	Buff	Ψ = -Ψ	10Γ sec	1-6	75%	—	Mir
Alcohol	Debuff	C /= (100/2^Γ)% T *= (100/10^Γ)%	10Γ sec -> +Zzz(Γ-1)	1-3	80%+15W%+5Γ%	Caffeine	Dru
Caffeine	Buff	C *= (100/2^Γ)% T *= (100/5^Γ)%	-Zzz2Γ -> 10Γ sec	1-3	90%+5P%+5Γ%	Alcohol 	Caf
Insta-kill	Debuff	H -= 1.5m	Ins	1-3	91%+3Γ%	—	Kil

Buffs: 11 Debuffs: 12
Other: 5 Effects: 28

Potions:

Effect	Ranks	Color	Hex	Opposite color	Opposite hex
Rgn	1-5	Pink	#FF4040	Dark green	#004000
Pro	1-5	Blue	#0000FF	Orange	#FF8700
You	1-3	Light blue	#4040FF	Dark brown	#402000
Str	1-5	Navy blue	#000033	Tan	#FFFFCC
Spe	1-3	Light gray	#BBBBBB	Dark gray	#404040
Lck	1-3	Light green	#40FF40	Dark red	#400000
Big	1-5	Purple	#870087	Yellow	#FFFF00
Caf	1-3	Brown	#874000	Magenta	#FF00FF
Clr	1	Clear	#00000000	—	—
Cur	1	White	#FFFFFF	Black	#000000
Amp	1-3	Peach	#A06000	Maroon	#872000

100% chance of working
If there is opposite, then 10% chance of being opposite
2 of the same potion make one of that potion, but the next rank

Level-Up:

τ usage:
•	M *= 110%
•	N *= 110%
•	Q += 1
•	D *= 1
•	T += 10%
•	V -= 10%
•	R += 1 O += 1
•	C -= 1
•	P += 10% W -= 5
-, I, II, III, IV, V, VI, VII, VIII, IX, X, MAX

Equations:
U = 50*2^((L+2)%3)*10^(L//3)
I += 10%
Y += 10
τ += 1
ζ += (((L-1)%3)+1)%2

Clocks:

Every C sec, attack

Every 1 sec, if R==0, then skip until •; else, then do not skip

α: R<0

H += (2^(|R|-1))(-1^α)

•

Every 1 sec, if O==0, then skip until •; if R<4M/5, then skip until •; else, then do not skip

α: O<0

S += (2^(|O|-1))(-1^α)

Character:

Race:
Race	Ring name	Ring Color	Ring Hex	Ring power
Troll	Ring of Darkness	Black	000000	D *= (100+2Φ)%
Elf	Ring of Light	White	FFFFFF	C /= (100+2Φ)%
Human	Ring of the Mind	Grey	878787	D *= (100+Φ)% C /= (100+Φ)%


Evolution:
Race	Evolution	Ring power
Troll	Golem	D *= (100+4Φ)% J += Amp3
Elf	High Elf	C /= (100+2Φ)% J += Amp3
Human	Cyborg	D *= (100+2Φ)% C /= (100+2Φ)% J += Amp3

Evolution Ring is given after completing the main game
Evolution Ring replaces Race Ring

Class:
Class	Ring name	Ring Color	Ring Hex	Ring power
Cleric	Ring of Healing	Red	FF0000	M *= (100+2Φ)% R *= (100+2Φ)% N *= (100-0.5Φ)% O *= (100-0.5Φ)%
Sorcerer	Ring of Magic	Blue	0000FF	N *= (100+2Φ)% O *= (100+2Φ)% X *= (100-0.5Φ)% E *= (100-0.5Φ)%
Rogue	Ring of Greed	Dark green	008000	X *= (100+2Φ)% E *= (100+2Φ)% M *= (100-0.5Φ)% R *= (100-0.5Φ)%


Sub-Class:
Class	Sub-Class	Ring Name	Ring Color	Ring Hex	Ring power
Cleric	Monk	Ring of Faith	Purple	8700A9	M *= (100+10Φ)% R *= (100+2Φ)% N *= (100-0.5Φ)% O *= (100-0.5Φ)%
Cleric	Medic	Ring of Life	Yellow	878700	M *= (100+2Φ)% R *= (100+10Φ)% N *= (100-0.5Φ)% O *= (100-0.5Φ)%
Sorcerer	Mage	Ring of Wisdom	Sky blue	40FF40	N *= (100+10Φ)% O *= (100+2Φ)% X *= (100-0.5Φ)% E *= (100-0.5Φ)%
Sorcerer	Wizard	Ring of Spellcasting	Navy	000040	N *= (100+2Φ)% O *= (100+10Φ)% X *= (100-0.5Φ)% E *= (100-0.5Φ)%
Rogue	Outlaw	Ring of Crime	Brown	634200	X *= (100+10Φ)% E *= (100+2Φ)% M *= (100-0.5Φ)% R *= (100-0.5Φ)%
Rogue	Thief	Ring of Theft	Green	00FF00	X *= (100+2Φ)% E *= (100+10Φ)% M *= (100-0.5Φ)% R *= (100-0.5Φ)%

Sub-Class Ring is chosen after beating the first tower
Sub-Class Ring replaces Class Ring

Mastery:
Sub-Class	Morality	Master	Ring power
Monk	Good	Angel	M *= (100+10Φ)% R *= (100+2Φ)% P *= (100+10Φ)% W *= (100-2Φ)%
Monk	Evil	Demon	M *= (100+10Φ)% R *= (100+2Φ)% P *= (100+2Φ)% W *= (100-10Φ)%
Medic	Good	Doctor	M *= (100+2Φ)% R *= (100+10Φ)% P *= (100+10Φ)% W *= (100-2Φ)%
Medic	Evil	Necromancer	M *= (100+2Φ)% R *= (100+10Φ)% P *= (100+2Φ)% W *= (100-10Φ)%
Mage	Good	Prophet	N *= (100+10Φ)% O *= (100+2Φ)% P *= (100+10Φ)% W *= (100-2Φ)%
Mage	Evil	Warlock	N *= (100+10Φ)% O *= (100+2Φ)% P *= (100+2Φ)% W *= (100-10Φ)%
Wizard	Good	Enchanter	N *= (100+2Φ)% O *= (100+10Φ)% P *= (100+10Φ)% W *= (100-2Φ)%
Wizard	Evil	Witch	N *= (100+2Φ)% O *= (100+10Φ)% P *= (100+2Φ)% W *= (100-10Φ)%
Outlaw	Good	Robin Hood	X *= (100+10Φ)% E *= (100+2Φ)% P *= (100+10Φ)% W *= (100-2Φ)%
Outlaw	Evil	Criminal 	X *= (100+10Φ)% E *= (100+2Φ)% P *= (100+2Φ)% W *= (100-10Φ)%
Thief	Good	Raider	X *= (100+2Φ)% E *= (100+10Φ)% P *= (100+10Φ)% W *= (100-2Φ)%
Thief	Evil	Robber	X *= (100+2Φ)% E *= (100+10Φ)% P *= (100+2Φ)% W *= (100-10Φ)%

Master Ring is chosen after completing the main game
Master Ring replaces Sub-Class Ring


Personalization:
•	Name
•	Gender
1.	Boy
2.	Girl

Currencies:
Name	Use	Symbol
Market Points	Items	μ
Skill Points	Skill Tree	ζ
Trait Points	Stats	τ
Upgrade Points	Gear	υ
Potion Points	Potions	ν


Earning:
μ —— selling items
υ —— loot
τ —— leveling up
ζ —— leveling up
ν —— shop

Enemies:
Name	Abbreviation	κ	ρ	Lines	M	R	N	O	D	C	B	K	A	T	V	G	F	P	W	x
Dummy	Tu	Dojo	0	"…"	10	0	0	0	0	0	0	—	0	0%	100%	—	—	100%	100%	0
Zombie	Da	Dead	1	"Braaaiiiiins…"																
Skeleton	Db	Dead	2	"{Rattle rattle}"																
Ghost	Dc	Dead	3	"BOO!" "OOooOOooOOoo…"																
Spirit	Dd	Dead	4	"Hhheelllppp mmmeee"																
Death	Df	Dead	BOSS	"Death comes for you all" "You will soon be mine, one way or another." "Prepare to-uuuhhh-die."																
Robot	Fa	Future	1	"Beep" "Boop"																
Scientist	Fb	Future	2	"Eureka!"																
Alien	Fc	Future	3	"We come in peace" "Afhjusdhhtüę"																
UFO	Fd	Future	4	"{Whirring sound}"																
AI	Ff	Future	BOSS	"Natural life is a disease" "ERROR"																
Harpies	Ma	Myth	1	"Caw! Caw!"																
Minotaur	Mb	Myth	2	"{Angrily grunts}"																
Gorgon	Mc	Myth	3	"Hissssss"								Pet2								
Nemean Lion	Md	Myth	4	"ROOAARR!"									60%							
Hydra	Mf	Myth	BOSS	"{licks lips menacingly}"								Poi5								
Porr-Ta’al i	Va	Victory	BOSS	"You will NEVER defeat me!" "{Evil laugh}"																
Porr-Ta’al ii	Vb	Victory	BOSS	"Is that the best you’ve got?!" "Those portals will NEVER close!"																
Porr-Ta’al iii	Vc	Victory	BOSS	"I won’t be defeated by the likes of you!" "You can’t beat my final form!"																
Fans	Ba	Fame	1	"Can I have your autograph!?" "Marry me!" "I love you!" "I’m your biggest fan!"																
Paparazzi	Bb	Fame	2	"{Takes a picture}"																
Media	Bc	Fame	3	"Scandal!" "BREAKING NEWS" "Conspiracy?" "Illuminati confirmed!"																
Agent	Bf	Fame	BOSS	"Sell out!" "You should make a guest appearance here!" "You’ve gone out of style!" "Sell these Funco-Pops!"																


Loot:
Getting:
If ρ is BOSS, then Λ is unique; if ρ is 0, then you get nothing; else, then:

I% of finding anything

Ξ: lesser of ρ and Q

Π: (20(5-Q))% of normal; 20Q% of κ

Specials:
Boss	Special	Use
Death	Scythe	If H==0, then H = 20M% K += Poi10
AI	Processor	C /= 150% If T<100%, then T = 100%
Dragon	Scale	K += Fir3 If A<90%, then A = 90%
Porr-Ta’al	Amulet	K += Kil3


Skill Tree:
Skills:
Name	Abbreviation	Category	Use	Applied	Levels	Icon
Sweep	We	Attacking	Every fifth attack, hit every enemy at once, with β/3 of Ψ for each one; K is only used for target	Weapon	3	Sword pointing straight up; straight movement lines to left of sword
Swing	Sw	Attacking	Every other attack, also attack the two neighboring enemies of the target, with Ψ/2 for each one; K is only used for target	Weapon	1	Sword pointing to top-right; a curved movement line to bottom-right of sword
Multi-Strike	Ms	Attacking	Every third attack, attack β+1 times; counts as 1 attack; K is only used on first attack; as soon as one of the attacks miss, stop	Sword	2	Sword pointing to top-left
Flurry	Fl	Attacking	Every third attack, attack β+1 times; counts as 1 attack; K is only used on first attack; as soon as one of the attacks miss, stop	Bow	2	Bow with arrow pointing to top-left
Last Stand	Ls	Life	While H<=M/10, R += 1	Any	1	A heart; an exclamation point inside of the heart
Leach	Le	Life	Every attack, if critical, then H += Ψ/2; else, then (50+10β)% chance of H += Ψ/2	Sword	4	A heart; an arrow pointing to the right, inside of the heart
Limit	Lm	Rewards	Every time you get loot, if Ξ<β+1, then get rid of the item	Any	3	A square on the left and on the right; greater-than sign in the center
Cap	Cp	Rewards	Every time you get loot, if you already have that item, don’t pick up the new one	Any	1	"x1" in center
Spikes	Sp	Attacking/Life	Every time an enemy hits you, if not critical, then Ψ += D/5	Shield 	1	Shield in center; spike pointing straight up, inside of the shield
Timing	Ti	Attacking/Rewards	Every time that you kill an enemy with a critical attack, Q += 1	Any	1	Plus in center
Close Call	Cc	Life/Rewards	Every time that you kill an enemy, if H <= M/10, then I = 100%	Any	1	Square in center; exclamation point in the square
Help	He	Attacking/Life/Rewards	Every other time that you kill an enemy, then 20% chance of D *= 110%, or 20% chance of H += M/20, or 20% chance of Q += 1, or 40% of nothing	Any	1	Percent sign in center

Skills cost βζ

Layout:
Skill	Needed
Sweep I	Sw1
Sweep II	We1
Sweep III	We2
Swing	—
Multi-Strike I	Sw1
Multi-Strike II	Ms1
Flurry I	Sw1
Flurry II	Fl1
Last Stand	—
Leach I	Ls1
Leach II	Le1
Leach III	Le2
Leach IV	Le3
Limit I	Cp1
Limit II	Lm1
Limit III	Lm2
Cap	—
Spikes	We3, Le4
Timing	We3, Lm3
Close Call	Le4, Lm3
Help	Sp1, Ti1, Cc1


Style:
 

Map:

 

Poems:

Set-up:
Every hero has to have
A gender,
A tribe,
A name.
Before going out
To save the day.

Start:
Time to get started
Playing this game.
Ready, set, go!
Get fortune and fame.

Dojo:
Healing cleric,
Magical sorcerer,
Greedy rogue,
Which class will you pick?

Towers:
Apocalyptic.
AI-prolific.
Ancient and mythic.

Win:
You did it!
You have won!
Keep going,
Or are you done?

Done:
A job well done!
Wanna play again?
That was fun!

Bonus:
You now have
Fortune and fame.
Everyone,
Elf, troll, or human
Now knows your name.

Death:
You died.
At least
You tried.

Save:
Save your progress!
If you don’t,
Regress.

Complete:
Verse 1:

Elf of the light;
Now a high elf,
With much might.

OR

Troll of the dark;
Now a Golem,
And a monarch.

OR

Human of the mind;
Now a Cyborg,
Who can’t be confined.

Verse 2, first half:

Healing cleric,
And then a monk;

OR

Healing cleric,
And then a medic;

OR

Magic sorcerer,
And then a mage;

OR

Magic sorcerer,
And then a wizard;

OR

Greedy rogue,
And then an outlaw;

OR

Greedy rogue,
And then a thief;

Verse 2, second half:

Turned good,
So is angelic.

OR

Turned evil,
So is demonic.

OR

Turned good,
So has a doctorate.

OR

Turned evil,
So is necromantic.

OR

Turned good,
So is prophetic and has old
age.

OR

Turned evil,
So is a warlock that goes into
rage.

OR

Turned good,
So is an enchanter.

OR

Turned evil,
So a witch and a caster.

OR

Turned good,
So like H and D surrounding
two Os.

OR

Turned evil,
So in a jail-cell and left to
rot.

OR

Turned good,
So raids the wealthy.

OR

Turned evil,
So robs homes.

Verse 3:

Village habitat.
Practice makes perfect.
Apocalyptic.
AI-prolific.
Ancient and mystic.
Triumphant.
Successfully have gone through
it.
You are terrific!

Verse 4:

You’re a star!
Do you want to restart?
Or if you are done,
I sure hope you had fun!

Verse 5:
If you play again,
Then don’t play the same!
Because what you choose
matters!

Verse 6:
GOOD GAME

Order:
1.	Default
2.	Rings
1.	*=
2.	/=
3.	=
4.	+=
5.	-=
3.	Gear
1.	Feet
1.	*=
2.	/=
3.	=
4.	+=
5.	-=
2.	Legs
1.	*=
2.	/=
3.	=
4.	+=
5.	-=
3.	Chest
1.	*=
2.	/=
3.	=
4.	+=
5.	-=
4.	Head
1.	*=
2.	/=
3.	=
4.	+=
5.	-=
5.	Hands
1.	Left
1.	*=
2.	/=
3.	=
4.	+=
5.	-=
2.	Right
1.	*=
2.	/=
3.	=
4.	+=
5.	-=
4.	Skills
1.	{ordered via hard-coded list}
1.	*=
2.	/=
3.	=
4.	+=
5.	-=
5.	Effects
1.	{ordered by time added oldest>newest}
1.	*=
2.	/=
3.	=
4.	+=
5.	-=
6.	Special
1.	*=
2.	/=
3.	=
4.	+=
5.	-=

Settings:
•	Audio
o	Music (%)
o	Sound effects (%)
o	
•	Visual
o	Brightness (%)
o	Text
	Font
	Arial
	Times New Roman
	…
	Font color (color)
	Size
1.	Tiny
2.	Small
3.	Medium
4.	Large
5.	Huge
o	UI color (color)
•	Game
o	Difficulty
1.	Easy
2.	Normal
3.	Hard
o	Autosave
	Off
	1 min
	5 min
	10 min
o	Controls
	…

Music:

https://drive.google.com/drive/folders/17RK4-6tdNn8EN4EP6aeKDQqLwDkoHIwg

•	Poems
•	Inventory
•	Map
•	Battle
•	Shop
•	Theme
•	Game over
•	Pause
•	Settings 
•	Bosses
•	House
•	Dojo
•	Dead Tower
•	Future Tower
•	Myth Tower
•	Mansion of Fame
•	Character creation
•	Credits
•	Special 
•	Skill tree
•	Cut-scenes
•	Low health
•	Saving
•	Win
•	Cauldron
•	Loading
•	Potions
•	Finale (good)
•	Finale (evil)
•	Achievements

Andrew’s stuff:
Upload to this link, with the name given on the list:

https://drive.google.com/drive/folders/1--r04CpFQwER5T88H5kQHbddk00Jrf-j

•	Male human character back
•	Male human character front
•	Female human character back
•	Female human character front
•	Male elf character back 
•	Male elf character front
•	Female elf character back
•	Female elf character front
•	Male troll character back
•	Male troll character front 
•	Female troll character back
•	Female troll character front 
•	Male cyborg character back
•	Male cyborg character front 
•	Female cyborg character back 
•	Female cyborg character front 
•	Male high elf character back
•	Male high elf character front
•	Female high elf character back
•	Female high elf character front 
•	Male golem character back
•	Male golem character front
•	Female golem character back
•	Female golem character front 

Achievements:
Name	Goal	Icon	Category	Description
Completionist	Unlock every achievement listed below	Trophy; crown on top-right of trophy	Platinum 	Amazing!
Happy Birthday!	Finish creating your character	Three balloons, with strings connected at bottom	Plastic	You exist now! Good job!
Get a Job!	Leave your house	House	Plastic	Being a hero isn’t a real job.
Learning	Get the Stat-Band	Stat-Band	Plastic	Make sure not to brea- oh.
Wax On, Wax Off	Finish the tutorial	Fist, off-centered to the bottom-left; counterclockwise movement lines next to hand	Plastic	A single day of training is enough, right?
Murderer! I	Kill an enemy	Bone	Plastic	HOW COULD YOU!?
Murderer! II	Kill 50 enemies	Skull	Bronze	{barfs while sobbing}
Murderer! III	Kill 100 enemies	Three skulls	Bronze	AAAAAAHHHHHH!!!!!
Murderer! IV	Kill 500 enemies	Pile of skulls	Silver	WHY ARE YOU DOING THIS!?
Murderer! V	Kill 1,000 enemies	Grid of skulls	Gold	{dies}
Goodbye.	Die	Grave; RIP on gravestone	Plastic	RIP
Gimme!	Buy something	Dollar sign	Bronze	It’s on sale!
Money!	Sell something	Present	Bronze	$$$
Immortal	Kill Death	Scythe; drop of blood dripping from tip of scythe	Gold	Death has died! …how?
ERROR!	Kill the AI	Computer chip	Gold	404 Description not found
Roar!	Kill the dragon	Dragon’s mouth, open; fire coming out of mouth	Gold	Wait, that’s not from greek mytholo-
The End	Kill Porr Ta’al	Portal	Platinum 	You did it!
El Fin	Fire your agent	Overflowing suitcase 	Platinum 	I’m Your Biggest Fan!!!
Talented	Get every skill	Tree	Platinum 	Show-off!
Beginner	Reach level 25	Baby head	Bronze	1 quarter to max level!
Average	Reach level 50	Kid head	Silver	Halfway to max level!
Pro	Reach level 75	Adult head	Gold	1 quarter left until max level!
Master	Reach level 100	Elderly head	Platinum 	MAX LEVEL!!!


Stages:
Dojo:
Floor	Room	Enemies
1	1	/-/-/-Tu-/-/-/
1	2	/-/-Tu-Tu-Tu-/-/
2	1	/-/-/-Tu-/-/-/
2	2	/-/-Tu-Tu-/-/-/
3	1	/-/-/-Tu-/-/-/
3	2	/-/-/-Tu-/-/-/
3	3	/-/-/-Tu-/-/-/


Dead Tower:
Floor	Room	Enemies
1	1	
2	1	
3	1	
Boss	1	/-/-/-Df-/-/-/


Future Tower:
Floor	Room	Enemies
1	1	
2	1	
3	1	
Boss	1	/-/-/-Ff-/-/-/


Myth Tower:
Floor	Room	Enemies
1	1	
2	1	
3	1	
Boss	1	/-/-/-Mf-/-/-/


Tower of Victory:
Floor	Room	Enemies
Boss	1	/-/-/-Va-/-/-/
Boss	2	/-/-/-Vb-/-/-/
Boss	3	/-/-/-Vc-/-/-/


Mansion of Fame:
Floor	Room	Enemies
1		
Boss	1	/-/-/-Bf-/-/-/


Stat-Band:

•	Stats
o	All
o	Health
o	Shield
o	Loot
o	Effects
o	Level
•	Gear
o	Inventory
o	Equipped
	Head
	Chest
	Legs
	Feet
	Left hand
	Right hand
	Left finger
	Right finger
	Back
o	Unequipped
•	Cauldron
o	Brew
o	Mix
•	Achievements
•	Settings
o	…
•	Quit

Controls:

General:
Action	Key
Back	Esc
Up/Down/Left/Right	Arrow keys/WASD
Select	Enter
Pause/Unpause	Space
Go through	Enter
Screenshot	Tab


Combat:
Action	Key
Special	Shift
Peek	Hover
Target	Left click


Inventory:
Action	Key
Select	Left-click
Stack all	Shift + left-click
Select some	Hold left-click
Swap	Left-click
Unselect	Left-click
Move	Enter
Replace	Double-left-click
Delete	Backspace


Other:
Place	Action	Key
Bedroom	Edit	Shift
		


House

Bedroom:
Item	Place	Size	Price	Max
Bed	Floor	2x1	Free	1
Chest	Floor	1x1	(5*2^χ)μ	—
Mural	Wall	3x3	Free	1
Painting	Wall	2x3	Free	2
Poster	Wall	3x2	Free	2
Banner	Wall	2x1	Free	10
Flag	Wall	1x2	Free	8
Portrait	Wall	2x2	Free	4
Picture	Wall	1x1	Free	20


Kitchen:
Item	Price
Fridge	5*2^χ
Microwave	5*2^χ


Item types:

Name	Categories	Slot(s)	Size	Stack	Use	From
Race Ring	Ring	RingR	1x1	1	Race	Character 
Evolution Ring	Ring	RingR	1x1	1	Evolution	Character 
Class Ring	Ring	RingC	1x1	1	Class	Character 
Sub-Class Ring	Ring	RingC	1x1	1	Sub-class	Character 
Master Ring	Ring	RingC	1x1	1	Mastery	Character 
Backpack	Bag	Back	2x2	1	Inventory	Shop
Sword	Sword, Weapon	HandL, HandR	2x1	2	|Offense stats	Loot, shop
Special 	Special	Special	3x2	1	Unique 	Boss loot
Bow	Bow, Weapon	HandL+HandR>HandL+HandR	2x1	1	Shoot arrows; ~offense stats	Loot, shop
Arrows	Ammo	*HandL, *HandR	1x1	64	Ammo for bow	Loot, shop
Dipped Arrows	Ammo	*HandL, *HandR	1x1	64	Ammo for bow; adds to K	Inventory, shop, loot
Shield 	Shield 	HandL, HandR	2x2	1	|Defense stats	Shop, loot
Boots	Clothes	Feet	1x2	1	Stats	Shop, loot
Leggings	Clothes	Legs	2x1	1	Stats	Shop, loot
Chestplate	Clothes	Torso	2x2	1	Stats	Shop, loot
Helmet	Clothes	Head	1x1	1	Stats	Shop, loot
Knife	Sword, Weapon	HandL, HandR	1x1	5	~Speed stats; offense stats	Shop, loot
Daggers	Sword, Weapon	HandL>>HandR, HandR>>HandL, **HandL, **HandR	1x1	2	|Speed stats; ~offense stats	Shop, loot
Crossbow	Bow, Weapon	HandL+HandR>HandL+HandR	2x1	1	Shoot arrows; offense stats	Shop, loot
Potion	Potion	—	1x1	5	Effects	Cauldron
Raw meat	Food	—	1x1	8	~Life stats; Poi	Loot
Cooked meat	Food	—	1x1	8	|Life stats	Kitchen
						
Plant	Food	—	1x1	16	Life stats	Shop
Stat-Band	Band	Wrist	1x1	1	Menus	Story
Note	Read	—	1x1	1	Read	Loot, story


Sent from my iPhone

