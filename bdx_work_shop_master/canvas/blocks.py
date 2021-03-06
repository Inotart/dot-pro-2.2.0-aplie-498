from collections import defaultdict
# the blocks_value_name is copied from MCEdit 2.0
# https://github.com/mcedit/mcedit2
# LICENSE: https://github.com/mcedit/mcedit2/blob/master/LICENSE.md  
BLOCKS_DEFINE=[
  [0, 0, "minecraft:air"],
  [1, 0, "minecraft:stone[variant=stone]"],
  [1, 1, "minecraft:stone[variant=granite]"],
  [1, 2, "minecraft:stone[variant=smooth_granite]"],
  [1, 3, "minecraft:stone[variant=diorite]"],
  [1, 4, "minecraft:stone[variant=smooth_diorite]"],
  [1, 5, "minecraft:stone[variant=andesite]"],
  [1, 6, "minecraft:stone[variant=smooth_andesite]"],
  [2, 0, "minecraft:grass[snowy=false]"],
  [3, 0, "minecraft:dirt[snowy=false,variant=dirt]"],
  [3, 1, "minecraft:dirt[snowy=false,variant=coarse_dirt]"],
  [3, 2, "minecraft:dirt[snowy=false,variant=podzol]"],
  [4, 0, "minecraft:cobblestone"],
  [5, 0, "minecraft:planks[variant=oak]"],
  [5, 1, "minecraft:planks[variant=spruce]"],
  [5, 2, "minecraft:planks[variant=birch]"],
  [5, 3, "minecraft:planks[variant=jungle]"],
  [5, 4, "minecraft:planks[variant=acacia]"],
  [5, 5, "minecraft:planks[variant=dark_oak]"],
  [6, 0, "minecraft:sapling[stage=0,type=oak]"],
  [6, 1, "minecraft:sapling[stage=0,type=spruce]"],
  [6, 2, "minecraft:sapling[stage=0,type=birch]"],
  [6, 3, "minecraft:sapling[stage=0,type=jungle]"],
  [6, 4, "minecraft:sapling[stage=0,type=acacia]"],
  [6, 5, "minecraft:sapling[stage=0,type=dark_oak]"],
  [6, 8, "minecraft:sapling[stage=1,type=oak]"],
  [6, 9, "minecraft:sapling[stage=1,type=spruce]"],
  [6, 10, "minecraft:sapling[stage=1,type=birch]"],
  [6, 11, "minecraft:sapling[stage=1,type=jungle]"],
  [6, 12, "minecraft:sapling[stage=1,type=acacia]"],
  [6, 13, "minecraft:sapling[stage=1,type=dark_oak]"],
  [7, 0, "minecraft:bedrock"],
  [8, 0, "minecraft:flowing_water[level=0]"],
  [8, 1, "minecraft:flowing_water[level=1]"],
  [8, 2, "minecraft:flowing_water[level=2]"],
  [8, 3, "minecraft:flowing_water[level=3]"],
  [8, 4, "minecraft:flowing_water[level=4]"],
  [8, 5, "minecraft:flowing_water[level=5]"],
  [8, 6, "minecraft:flowing_water[level=6]"],
  [8, 7, "minecraft:flowing_water[level=7]"],
  [8, 8, "minecraft:flowing_water[level=8]"],
  [8, 9, "minecraft:flowing_water[level=9]"],
  [8, 10, "minecraft:flowing_water[level=10]"],
  [8, 11, "minecraft:flowing_water[level=11]"],
  [8, 12, "minecraft:flowing_water[level=12]"],
  [8, 13, "minecraft:flowing_water[level=13]"],
  [8, 14, "minecraft:flowing_water[level=14]"],
  [8, 15, "minecraft:flowing_water[level=15]"],
  [9, 0, "minecraft:water[level=0]"],
  [9, 1, "minecraft:water[level=1]"],
  [9, 2, "minecraft:water[level=2]"],
  [9, 3, "minecraft:water[level=3]"],
  [9, 4, "minecraft:water[level=4]"],
  [9, 5, "minecraft:water[level=5]"],
  [9, 6, "minecraft:water[level=6]"],
  [9, 7, "minecraft:water[level=7]"],
  [9, 8, "minecraft:water[level=8]"],
  [9, 9, "minecraft:water[level=9]"],
  [9, 10, "minecraft:water[level=10]"],
  [9, 11, "minecraft:water[level=11]"],
  [9, 12, "minecraft:water[level=12]"],
  [9, 13, "minecraft:water[level=13]"],
  [9, 14, "minecraft:water[level=14]"],
  [9, 15, "minecraft:water[level=15]"],
  [10, 0, "minecraft:flowing_lava[level=0]"],
  [10, 1, "minecraft:flowing_lava[level=1]"],
  [10, 2, "minecraft:flowing_lava[level=2]"],
  [10, 3, "minecraft:flowing_lava[level=3]"],
  [10, 4, "minecraft:flowing_lava[level=4]"],
  [10, 5, "minecraft:flowing_lava[level=5]"],
  [10, 6, "minecraft:flowing_lava[level=6]"],
  [10, 7, "minecraft:flowing_lava[level=7]"],
  [10, 8, "minecraft:flowing_lava[level=8]"],
  [10, 9, "minecraft:flowing_lava[level=9]"],
  [10, 10, "minecraft:flowing_lava[level=10]"],
  [10, 11, "minecraft:flowing_lava[level=11]"],
  [10, 12, "minecraft:flowing_lava[level=12]"],
  [10, 13, "minecraft:flowing_lava[level=13]"],
  [10, 14, "minecraft:flowing_lava[level=14]"],
  [10, 15, "minecraft:flowing_lava[level=15]"],
  [11, 0, "minecraft:lava[level=0]"],
  [11, 1, "minecraft:lava[level=1]"],
  [11, 2, "minecraft:lava[level=2]"],
  [11, 3, "minecraft:lava[level=3]"],
  [11, 4, "minecraft:lava[level=4]"],
  [11, 5, "minecraft:lava[level=5]"],
  [11, 6, "minecraft:lava[level=6]"],
  [11, 7, "minecraft:lava[level=7]"],
  [11, 8, "minecraft:lava[level=8]"],
  [11, 9, "minecraft:lava[level=9]"],
  [11, 10, "minecraft:lava[level=10]"],
  [11, 11, "minecraft:lava[level=11]"],
  [11, 12, "minecraft:lava[level=12]"],
  [11, 13, "minecraft:lava[level=13]"],
  [11, 14, "minecraft:lava[level=14]"],
  [11, 15, "minecraft:lava[level=15]"],
  [12, 0, "minecraft:sand[variant=sand]"],
  [12, 1, "minecraft:sand[variant=red_sand]"],
  [13, 0, "minecraft:gravel"],
  [14, 0, "minecraft:gold_ore"],
  [15, 0, "minecraft:iron_ore"],
  [16, 0, "minecraft:coal_ore"],
  [17, 0, "minecraft:log[axis=y,variant=oak]"],
  [17, 1, "minecraft:log[axis=y,variant=spruce]"],
  [17, 2, "minecraft:log[axis=y,variant=birch]"],
  [17, 3, "minecraft:log[axis=y,variant=jungle]"],
  [17, 4, "minecraft:log[axis=x,variant=oak]"],
  [17, 5, "minecraft:log[axis=x,variant=spruce]"],
  [17, 6, "minecraft:log[axis=x,variant=birch]"],
  [17, 7, "minecraft:log[axis=x,variant=jungle]"],
  [17, 8, "minecraft:log[axis=z,variant=oak]"],
  [17, 9, "minecraft:log[axis=z,variant=spruce]"],
  [17, 10, "minecraft:log[axis=z,variant=birch]"],
  [17, 11, "minecraft:log[axis=z,variant=jungle]"],
  [17, 12, "minecraft:log[axis=none,variant=oak]"],
  [17, 13, "minecraft:log[axis=none,variant=spruce]"],
  [17, 14, "minecraft:log[axis=none,variant=birch]"],
  [17, 15, "minecraft:log[axis=none,variant=jungle]"],
  [18, 0, "minecraft:leaves[check_decay=false,decayable=true,variant=oak]"],
  [18, 1, "minecraft:leaves[check_decay=false,decayable=true,variant=spruce]"],
  [18, 2, "minecraft:leaves[check_decay=false,decayable=true,variant=birch]"],
  [18, 3, "minecraft:leaves[check_decay=false,decayable=true,variant=jungle]"],
  [18, 4, "minecraft:leaves[check_decay=false,decayable=false,variant=oak]"],
  [18, 5, "minecraft:leaves[check_decay=false,decayable=false,variant=spruce]"],
  [18, 6, "minecraft:leaves[check_decay=false,decayable=false,variant=birch]"],
  [18, 7, "minecraft:leaves[check_decay=false,decayable=false,variant=jungle]"],
  [18, 8, "minecraft:leaves[check_decay=true,decayable=true,variant=oak]"],
  [18, 9, "minecraft:leaves[check_decay=true,decayable=true,variant=spruce]"],
  [18, 10, "minecraft:leaves[check_decay=true,decayable=true,variant=birch]"],
  [18, 11, "minecraft:leaves[check_decay=true,decayable=true,variant=jungle]"],
  [18, 12, "minecraft:leaves[check_decay=true,decayable=false,variant=oak]"],
  [18, 13, "minecraft:leaves[check_decay=true,decayable=false,variant=spruce]"],
  [18, 14, "minecraft:leaves[check_decay=true,decayable=false,variant=birch]"],
  [18, 15, "minecraft:leaves[check_decay=true,decayable=false,variant=jungle]"],
  [19, 0, "minecraft:sponge[wet=false]"],
  [19, 1, "minecraft:sponge[wet=true]"],
  [20, 0, "minecraft:glass"],
  [21, 0, "minecraft:lapis_ore"],
  [22, 0, "minecraft:lapis_block"],
  [23, 0, "minecraft:dispenser[facing=down,triggered=false]"],
  [23, 1, "minecraft:dispenser[facing=up,triggered=false]"],
  [23, 2, "minecraft:dispenser[facing=north,triggered=false]"],
  [23, 3, "minecraft:dispenser[facing=south,triggered=false]"],
  [23, 4, "minecraft:dispenser[facing=west,triggered=false]"],
  [23, 5, "minecraft:dispenser[facing=east,triggered=false]"],
  [23, 8, "minecraft:dispenser[facing=down,triggered=true]"],
  [23, 9, "minecraft:dispenser[facing=up,triggered=true]"],
  [23, 10, "minecraft:dispenser[facing=north,triggered=true]"],
  [23, 11, "minecraft:dispenser[facing=south,triggered=true]"],
  [23, 12, "minecraft:dispenser[facing=west,triggered=true]"],
  [23, 13, "minecraft:dispenser[facing=east,triggered=true]"],
  [24, 0, "minecraft:sandstone[type=sandstone]"],
  [24, 1, "minecraft:sandstone[type=chiseled_sandstone]"],
  [24, 2, "minecraft:sandstone[type=smooth_sandstone]"],
  [25, 0, "minecraft:noteblock"],
  [26, 0, "minecraft:bed[facing=south,occupied=false,part=foot]"],
  [26, 1, "minecraft:bed[facing=west,occupied=false,part=foot]"],
  [26, 2, "minecraft:bed[facing=north,occupied=false,part=foot]"],
  [26, 3, "minecraft:bed[facing=east,occupied=false,part=foot]"],
  [26, 8, "minecraft:bed[facing=south,occupied=false,part=head]"],
  [26, 9, "minecraft:bed[facing=west,occupied=false,part=head]"],
  [26, 10, "minecraft:bed[facing=north,occupied=false,part=head]"],
  [26, 11, "minecraft:bed[facing=east,occupied=false,part=head]"],
  [26, 12, "minecraft:bed[facing=south,occupied=true,part=head]"],
  [26, 13, "minecraft:bed[facing=west,occupied=true,part=head]"],
  [26, 14, "minecraft:bed[facing=north,occupied=true,part=head]"],
  [26, 15, "minecraft:bed[facing=east,occupied=true,part=head]"],
  [27, 0, "minecraft:golden_rail[powered=false,shape=north_south]"],
  [27, 1, "minecraft:golden_rail[powered=false,shape=east_west]"],
  [27, 2, "minecraft:golden_rail[powered=false,shape=ascending_east]"],
  [27, 3, "minecraft:golden_rail[powered=false,shape=ascending_west]"],
  [27, 4, "minecraft:golden_rail[powered=false,shape=ascending_north]"],
  [27, 5, "minecraft:golden_rail[powered=false,shape=ascending_south]"],
  [27, 8, "minecraft:golden_rail[powered=true,shape=north_south]"],
  [27, 9, "minecraft:golden_rail[powered=true,shape=east_west]"],
  [27, 10, "minecraft:golden_rail[powered=true,shape=ascending_east]"],
  [27, 11, "minecraft:golden_rail[powered=true,shape=ascending_west]"],
  [27, 12, "minecraft:golden_rail[powered=true,shape=ascending_north]"],
  [27, 13, "minecraft:golden_rail[powered=true,shape=ascending_south]"],
  [28, 0, "minecraft:detector_rail[powered=false,shape=north_south]"],
  [28, 1, "minecraft:detector_rail[powered=false,shape=east_west]"],
  [28, 2, "minecraft:detector_rail[powered=false,shape=ascending_east]"],
  [28, 3, "minecraft:detector_rail[powered=false,shape=ascending_west]"],
  [28, 4, "minecraft:detector_rail[powered=false,shape=ascending_north]"],
  [28, 5, "minecraft:detector_rail[powered=false,shape=ascending_south]"],
  [28, 8, "minecraft:detector_rail[powered=true,shape=north_south]"],
  [28, 9, "minecraft:detector_rail[powered=true,shape=east_west]"],
  [28, 10, "minecraft:detector_rail[powered=true,shape=ascending_east]"],
  [28, 11, "minecraft:detector_rail[powered=true,shape=ascending_west]"],
  [28, 12, "minecraft:detector_rail[powered=true,shape=ascending_north]"],
  [28, 13, "minecraft:detector_rail[powered=true,shape=ascending_south]"],
  [29, 0, "minecraft:sticky_piston[extended=false,facing=down]"],
  [29, 1, "minecraft:sticky_piston[extended=false,facing=up]"],
  [29, 2, "minecraft:sticky_piston[extended=false,facing=north]"],
  [29, 3, "minecraft:sticky_piston[extended=false,facing=south]"],
  [29, 4, "minecraft:sticky_piston[extended=false,facing=west]"],
  [29, 5, "minecraft:sticky_piston[extended=false,facing=east]"],
  [29, 8, "minecraft:sticky_piston[extended=true,facing=down]"],
  [29, 9, "minecraft:sticky_piston[extended=true,facing=up]"],
  [29, 10, "minecraft:sticky_piston[extended=true,facing=north]"],
  [29, 11, "minecraft:sticky_piston[extended=true,facing=south]"],
  [29, 12, "minecraft:sticky_piston[extended=true,facing=west]"],
  [29, 13, "minecraft:sticky_piston[extended=true,facing=east]"],
  [30, 0, "minecraft:web"],
  [31, 0, "minecraft:tallgrass[type=dead_bush]"],
  [31, 1, "minecraft:tallgrass[type=tall_grass]"],
  [31, 2, "minecraft:tallgrass[type=fern]"],
  [32, 0, "minecraft:deadbush"],
  [33, 0, "minecraft:piston[extended=false,facing=down]"],
  [33, 1, "minecraft:piston[extended=false,facing=up]"],
  [33, 2, "minecraft:piston[extended=false,facing=north]"],
  [33, 3, "minecraft:piston[extended=false,facing=south]"],
  [33, 4, "minecraft:piston[extended=false,facing=west]"],
  [33, 5, "minecraft:piston[extended=false,facing=east]"],
  [33, 8, "minecraft:piston[extended=true,facing=down]"],
  [33, 9, "minecraft:piston[extended=true,facing=up]"],
  [33, 10, "minecraft:piston[extended=true,facing=north]"],
  [33, 11, "minecraft:piston[extended=true,facing=south]"],
  [33, 12, "minecraft:piston[extended=true,facing=west]"],
  [33, 13, "minecraft:piston[extended=true,facing=east]"],
  [34, 0, "minecraft:piston_head[facing=down,short=false,type=normal]"],
  [34, 1, "minecraft:piston_head[facing=up,short=false,type=normal]"],
  [34, 2, "minecraft:piston_head[facing=north,short=false,type=normal]"],
  [34, 3, "minecraft:piston_head[facing=south,short=false,type=normal]"],
  [34, 4, "minecraft:piston_head[facing=west,short=false,type=normal]"],
  [34, 5, "minecraft:piston_head[facing=east,short=false,type=normal]"],
  [34, 8, "minecraft:piston_head[facing=down,short=false,type=sticky]"],
  [34, 9, "minecraft:piston_head[facing=up,short=false,type=sticky]"],
  [34, 10, "minecraft:piston_head[facing=north,short=false,type=sticky]"],
  [34, 11, "minecraft:piston_head[facing=south,short=false,type=sticky]"],
  [34, 12, "minecraft:piston_head[facing=west,short=false,type=sticky]"],
  [34, 13, "minecraft:piston_head[facing=east,short=false,type=sticky]"],
  [35, 0, "minecraft:wool[color=white]"],
  [35, 1, "minecraft:wool[color=orange]"],
  [35, 2, "minecraft:wool[color=magenta]"],
  [35, 3, "minecraft:wool[color=light_blue]"],
  [35, 4, "minecraft:wool[color=yellow]"],
  [35, 5, "minecraft:wool[color=lime]"],
  [35, 6, "minecraft:wool[color=pink]"],
  [35, 7, "minecraft:wool[color=gray]"],
  [35, 8, "minecraft:wool[color=silver]"],
  [35, 9, "minecraft:wool[color=cyan]"],
  [35, 10, "minecraft:wool[color=purple]"],
  [35, 11, "minecraft:wool[color=blue]"],
  [35, 12, "minecraft:wool[color=brown]"],
  [35, 13, "minecraft:wool[color=green]"],
  [35, 14, "minecraft:wool[color=red]"],
  [35, 15, "minecraft:wool[color=black]"],
  [36, 0, "minecraft:piston_extension[facing=down,type=normal]"],
  [36, 1, "minecraft:piston_extension[facing=up,type=normal]"],
  [36, 2, "minecraft:piston_extension[facing=north,type=normal]"],
  [36, 3, "minecraft:piston_extension[facing=south,type=normal]"],
  [36, 4, "minecraft:piston_extension[facing=west,type=normal]"],
  [36, 5, "minecraft:piston_extension[facing=east,type=normal]"],
  [36, 8, "minecraft:piston_extension[facing=down,type=sticky]"],
  [36, 9, "minecraft:piston_extension[facing=up,type=sticky]"],
  [36, 10, "minecraft:piston_extension[facing=north,type=sticky]"],
  [36, 11, "minecraft:piston_extension[facing=south,type=sticky]"],
  [36, 12, "minecraft:piston_extension[facing=west,type=sticky]"],
  [36, 13, "minecraft:piston_extension[facing=east,type=sticky]"],
  [37, 0, "minecraft:yellow_flower[type=dandelion]"],
  [38, 0, "minecraft:red_flower[type=poppy]"],
  [38, 1, "minecraft:red_flower[type=blue_orchid]"],
  [38, 2, "minecraft:red_flower[type=allium]"],
  [38, 3, "minecraft:red_flower[type=houstonia]"],
  [38, 4, "minecraft:red_flower[type=red_tulip]"],
  [38, 5, "minecraft:red_flower[type=orange_tulip]"],
  [38, 6, "minecraft:red_flower[type=white_tulip]"],
  [38, 7, "minecraft:red_flower[type=pink_tulip]"],
  [38, 8, "minecraft:red_flower[type=oxeye_daisy]"],
  [39, 0, "minecraft:brown_mushroom"],
  [40, 0, "minecraft:red_mushroom"],
  [41, 0, "minecraft:gold_block"],
  [42, 0, "minecraft:iron_block"],
  [43, 0, "minecraft:double_stone_slab[seamless=false,variant=stone]"],
  [43, 1, "minecraft:double_stone_slab[seamless=false,variant=sandstone]"],
  [43, 2, "minecraft:double_stone_slab[seamless=false,variant=wood_old]"],
  [43, 3, "minecraft:double_stone_slab[seamless=false,variant=cobblestone]"],
  [43, 4, "minecraft:double_stone_slab[seamless=false,variant=brick]"],
  [43, 5, "minecraft:double_stone_slab[seamless=false,variant=stone_brick]"],
  [43, 6, "minecraft:double_stone_slab[seamless=false,variant=nether_brick]"],
  [43, 7, "minecraft:double_stone_slab[seamless=false,variant=quartz]"],
  [43, 8, "minecraft:double_stone_slab[seamless=true,variant=stone]"],
  [43, 9, "minecraft:double_stone_slab[seamless=true,variant=sandstone]"],
  [43, 10, "minecraft:double_stone_slab[seamless=true,variant=wood_old]"],
  [43, 11, "minecraft:double_stone_slab[seamless=true,variant=cobblestone]"],
  [43, 12, "minecraft:double_stone_slab[seamless=true,variant=brick]"],
  [43, 13, "minecraft:double_stone_slab[seamless=true,variant=stone_brick]"],
  [43, 14, "minecraft:double_stone_slab[seamless=true,variant=nether_brick]"],
  [43, 15, "minecraft:double_stone_slab[seamless=true,variant=quartz]"],
  [44, 0, "minecraft:stone_slab[half=bottom,variant=stone]"],
  [44, 1, "minecraft:stone_slab[half=bottom,variant=sandstone]"],
  [44, 2, "minecraft:stone_slab[half=bottom,variant=wood_old]"],
  [44, 3, "minecraft:stone_slab[half=bottom,variant=cobblestone]"],
  [44, 4, "minecraft:stone_slab[half=bottom,variant=brick]"],
  [44, 5, "minecraft:stone_slab[half=bottom,variant=stone_brick]"],
  [44, 6, "minecraft:stone_slab[half=bottom,variant=nether_brick]"],
  [44, 7, "minecraft:stone_slab[half=bottom,variant=quartz]"],
  [44, 8, "minecraft:stone_slab[half=top,variant=stone]"],
  [44, 9, "minecraft:stone_slab[half=top,variant=sandstone]"],
  [44, 10, "minecraft:stone_slab[half=top,variant=wood_old]"],
  [44, 11, "minecraft:stone_slab[half=top,variant=cobblestone]"],
  [44, 12, "minecraft:stone_slab[half=top,variant=brick]"],
  [44, 13, "minecraft:stone_slab[half=top,variant=stone_brick]"],
  [44, 14, "minecraft:stone_slab[half=top,variant=nether_brick]"],
  [44, 15, "minecraft:stone_slab[half=top,variant=quartz]"],
  [45, 0, "minecraft:brick_block"],
  [46, 0, "minecraft:tnt[explode=false]"],
  [46, 1, "minecraft:tnt[explode=true]"],
  [47, 0, "minecraft:bookshelf"],
  [48, 0, "minecraft:mossy_cobblestone"],
  [49, 0, "minecraft:obsidian"],
  [50, 0, "minecraft:torch[facing=up]"],
  [50, 1, "minecraft:torch[facing=east]"],
  [50, 2, "minecraft:torch[facing=west]"],
  [50, 3, "minecraft:torch[facing=south]"],
  [50, 4, "minecraft:torch[facing=north]"],
  [
    51,
    0,
    "minecraft:fire[age=0,east=false,north=false,south=false,up=false,west=false]"
  ],
  [
    51,
    1,
    "minecraft:fire[age=1,east=false,north=false,south=false,up=false,west=false]"
  ],
  [
    51,
    2,
    "minecraft:fire[age=2,east=false,north=false,south=false,up=false,west=false]"
  ],
  [
    51,
    3,
    "minecraft:fire[age=3,east=false,north=false,south=false,up=false,west=false]"
  ],
  [
    51,
    4,
    "minecraft:fire[age=4,east=false,north=false,south=false,up=false,west=false]"
  ],
  [
    51,
    5,
    "minecraft:fire[age=5,east=false,north=false,south=false,up=false,west=false]"
  ],
  [
    51,
    6,
    "minecraft:fire[age=6,east=false,north=false,south=false,up=false,west=false]"
  ],
  [
    51,
    7,
    "minecraft:fire[age=7,east=false,north=false,south=false,up=false,west=false]"
  ],
  [
    51,
    8,
    "minecraft:fire[age=8,east=false,north=false,south=false,up=false,west=false]"
  ],
  [
    51,
    9,
    "minecraft:fire[age=9,east=false,north=false,south=false,up=false,west=false]"
  ],
  [
    51,
    10,
    "minecraft:fire[age=10,east=false,north=false,south=false,up=false,west=false]"
  ],
  [
    51,
    11,
    "minecraft:fire[age=11,east=false,north=false,south=false,up=false,west=false]"
  ],
  [
    51,
    12,
    "minecraft:fire[age=12,east=false,north=false,south=false,up=false,west=false]"
  ],
  [
    51,
    13,
    "minecraft:fire[age=13,east=false,north=false,south=false,up=false,west=false]"
  ],
  [
    51,
    14,
    "minecraft:fire[age=14,east=false,north=false,south=false,up=false,west=false]"
  ],
  [
    51,
    15,
    "minecraft:fire[age=15,east=false,north=false,south=false,up=false,west=false]"
  ],
  [52, 0, "minecraft:mob_spawner"],
  [53, 0, "minecraft:oak_stairs[facing=east,half=bottom,shape=straight]"],
  [53, 1, "minecraft:oak_stairs[facing=west,half=bottom,shape=straight]"],
  [53, 2, "minecraft:oak_stairs[facing=south,half=bottom,shape=straight]"],
  [53, 3, "minecraft:oak_stairs[facing=north,half=bottom,shape=straight]"],
  [53, 4, "minecraft:oak_stairs[facing=east,half=top,shape=straight]"],
  [53, 5, "minecraft:oak_stairs[facing=west,half=top,shape=straight]"],
  [53, 6, "minecraft:oak_stairs[facing=south,half=top,shape=straight]"],
  [53, 7, "minecraft:oak_stairs[facing=north,half=top,shape=straight]"],
  [54, 0, "minecraft:chest[facing=north]"],
  [54, 3, "minecraft:chest[facing=south]"],
  [54, 4, "minecraft:chest[facing=west]"],
  [54, 5, "minecraft:chest[facing=east]"],
  [
    55,
    0,
    "minecraft:redstone_wire[east=none,north=none,power=0,south=none,west=none]"
  ],
  [
    55,
    1,
    "minecraft:redstone_wire[east=none,north=none,power=1,south=none,west=none]"
  ],
  [
    55,
    2,
    "minecraft:redstone_wire[east=none,north=none,power=2,south=none,west=none]"
  ],
  [
    55,
    3,
    "minecraft:redstone_wire[east=none,north=none,power=3,south=none,west=none]"
  ],
  [
    55,
    4,
    "minecraft:redstone_wire[east=none,north=none,power=4,south=none,west=none]"
  ],
  [
    55,
    5,
    "minecraft:redstone_wire[east=none,north=none,power=5,south=none,west=none]"
  ],
  [
    55,
    6,
    "minecraft:redstone_wire[east=none,north=none,power=6,south=none,west=none]"
  ],
  [
    55,
    7,
    "minecraft:redstone_wire[east=none,north=none,power=7,south=none,west=none]"
  ],
  [
    55,
    8,
    "minecraft:redstone_wire[east=none,north=none,power=8,south=none,west=none]"
  ],
  [
    55,
    9,
    "minecraft:redstone_wire[east=none,north=none,power=9,south=none,west=none]"
  ],
  [
    55,
    10,
    "minecraft:redstone_wire[east=none,north=none,power=10,south=none,west=none]"
  ],
  [
    55,
    11,
    "minecraft:redstone_wire[east=none,north=none,power=11,south=none,west=none]"
  ],
  [
    55,
    12,
    "minecraft:redstone_wire[east=none,north=none,power=12,south=none,west=none]"
  ],
  [
    55,
    13,
    "minecraft:redstone_wire[east=none,north=none,power=13,south=none,west=none]"
  ],
  [
    55,
    14,
    "minecraft:redstone_wire[east=none,north=none,power=14,south=none,west=none]"
  ],
  [
    55,
    15,
    "minecraft:redstone_wire[east=none,north=none,power=15,south=none,west=none]"
  ],
  [56, 0, "minecraft:diamond_ore"],
  [57, 0, "minecraft:diamond_block"],
  [58, 0, "minecraft:crafting_table"],
  [59, 0, "minecraft:wheat[age=0]"],
  [59, 1, "minecraft:wheat[age=1]"],
  [59, 2, "minecraft:wheat[age=2]"],
  [59, 3, "minecraft:wheat[age=3]"],
  [59, 4, "minecraft:wheat[age=4]"],
  [59, 5, "minecraft:wheat[age=5]"],
  [59, 6, "minecraft:wheat[age=6]"],
  [59, 7, "minecraft:wheat[age=7]"],
  [60, 0, "minecraft:farmland[moisture=0]"],
  [60, 1, "minecraft:farmland[moisture=1]"],
  [60, 2, "minecraft:farmland[moisture=2]"],
  [60, 3, "minecraft:farmland[moisture=3]"],
  [60, 4, "minecraft:farmland[moisture=4]"],
  [60, 5, "minecraft:farmland[moisture=5]"],
  [60, 6, "minecraft:farmland[moisture=6]"],
  [60, 7, "minecraft:farmland[moisture=7]"],
  [61, 0, "minecraft:furnace[facing=north]"],
  [61, 3, "minecraft:furnace[facing=south]"],
  [61, 4, "minecraft:furnace[facing=west]"],
  [61, 5, "minecraft:furnace[facing=east]"],
  [62, 0, "minecraft:lit_furnace[facing=north]"],
  [62, 3, "minecraft:lit_furnace[facing=south]"],
  [62, 4, "minecraft:lit_furnace[facing=west]"],
  [62, 5, "minecraft:lit_furnace[facing=east]"],
  [63, 0, "minecraft:standing_sign[rotation=0]"],
  [63, 1, "minecraft:standing_sign[rotation=1]"],
  [63, 2, "minecraft:standing_sign[rotation=2]"],
  [63, 3, "minecraft:standing_sign[rotation=3]"],
  [63, 4, "minecraft:standing_sign[rotation=4]"],
  [63, 5, "minecraft:standing_sign[rotation=5]"],
  [63, 6, "minecraft:standing_sign[rotation=6]"],
  [63, 7, "minecraft:standing_sign[rotation=7]"],
  [63, 8, "minecraft:standing_sign[rotation=8]"],
  [63, 9, "minecraft:standing_sign[rotation=9]"],
  [63, 10, "minecraft:standing_sign[rotation=10]"],
  [63, 11, "minecraft:standing_sign[rotation=11]"],
  [63, 12, "minecraft:standing_sign[rotation=12]"],
  [63, 13, "minecraft:standing_sign[rotation=13]"],
  [63, 14, "minecraft:standing_sign[rotation=14]"],
  [63, 15, "minecraft:standing_sign[rotation=15]"],
  [
    64,
    0,
    "minecraft:wooden_door[facing=east,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    64,
    1,
    "minecraft:wooden_door[facing=south,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    64,
    2,
    "minecraft:wooden_door[facing=west,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    64,
    3,
    "minecraft:wooden_door[facing=north,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    64,
    4,
    "minecraft:wooden_door[facing=east,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    64,
    5,
    "minecraft:wooden_door[facing=south,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    64,
    6,
    "minecraft:wooden_door[facing=west,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    64,
    7,
    "minecraft:wooden_door[facing=north,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    64,
    8,
    "minecraft:wooden_door[facing=north,half=upper,hinge=left,open=false,powered=false]"
  ],
  [
    64,
    9,
    "minecraft:wooden_door[facing=north,half=upper,hinge=right,open=false,powered=false]"
  ],
  [
    64,
    10,
    "minecraft:wooden_door[facing=north,half=upper,hinge=left,open=false,powered=true]"
  ],
  [
    64,
    11,
    "minecraft:wooden_door[facing=north,half=upper,hinge=right,open=false,powered=true]"
  ],
  [65, 0, "minecraft:ladder[facing=north]"],
  [65, 3, "minecraft:ladder[facing=south]"],
  [65, 4, "minecraft:ladder[facing=west]"],
  [65, 5, "minecraft:ladder[facing=east]"],
  [66, 0, "minecraft:rail[shape=north_south]"],
  [66, 1, "minecraft:rail[shape=east_west]"],
  [66, 2, "minecraft:rail[shape=ascending_east]"],
  [66, 3, "minecraft:rail[shape=ascending_west]"],
  [66, 4, "minecraft:rail[shape=ascending_north]"],
  [66, 5, "minecraft:rail[shape=ascending_south]"],
  [66, 6, "minecraft:rail[shape=south_east]"],
  [66, 7, "minecraft:rail[shape=south_west]"],
  [66, 8, "minecraft:rail[shape=north_west]"],
  [66, 9, "minecraft:rail[shape=north_east]"],
  [67, 0, "minecraft:stone_stairs[facing=east,half=bottom,shape=straight]"],
  [67, 1, "minecraft:stone_stairs[facing=west,half=bottom,shape=straight]"],
  [67, 2, "minecraft:stone_stairs[facing=south,half=bottom,shape=straight]"],
  [67, 3, "minecraft:stone_stairs[facing=north,half=bottom,shape=straight]"],
  [67, 4, "minecraft:stone_stairs[facing=east,half=top,shape=straight]"],
  [67, 5, "minecraft:stone_stairs[facing=west,half=top,shape=straight]"],
  [67, 6, "minecraft:stone_stairs[facing=south,half=top,shape=straight]"],
  [67, 7, "minecraft:stone_stairs[facing=north,half=top,shape=straight]"],
  [68, 0, "minecraft:wall_sign[facing=north]"],
  [68, 3, "minecraft:wall_sign[facing=south]"],
  [68, 4, "minecraft:wall_sign[facing=west]"],
  [68, 5, "minecraft:wall_sign[facing=east]"],
  [69, 0, "minecraft:lever[facing=down_x,powered=false]"],
  [69, 1, "minecraft:lever[facing=east,powered=false]"],
  [69, 2, "minecraft:lever[facing=west,powered=false]"],
  [69, 3, "minecraft:lever[facing=south,powered=false]"],
  [69, 4, "minecraft:lever[facing=north,powered=false]"],
  [69, 5, "minecraft:lever[facing=up_z,powered=false]"],
  [69, 6, "minecraft:lever[facing=up_x,powered=false]"],
  [69, 7, "minecraft:lever[facing=down_z,powered=false]"],
  [69, 8, "minecraft:lever[facing=down_x,powered=true]"],
  [69, 9, "minecraft:lever[facing=east,powered=true]"],
  [69, 10, "minecraft:lever[facing=west,powered=true]"],
  [69, 11, "minecraft:lever[facing=south,powered=true]"],
  [69, 12, "minecraft:lever[facing=north,powered=true]"],
  [69, 13, "minecraft:lever[facing=up_z,powered=true]"],
  [69, 14, "minecraft:lever[facing=up_x,powered=true]"],
  [69, 15, "minecraft:lever[facing=down_z,powered=true]"],
  [70, 0, "minecraft:stone_pressure_plate[powered=false]"],
  [70, 1, "minecraft:stone_pressure_plate[powered=true]"],
  [
    71,
    0,
    "minecraft:iron_door[facing=east,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    71,
    1,
    "minecraft:iron_door[facing=south,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    71,
    2,
    "minecraft:iron_door[facing=west,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    71,
    3,
    "minecraft:iron_door[facing=north,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    71,
    4,
    "minecraft:iron_door[facing=east,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    71,
    5,
    "minecraft:iron_door[facing=south,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    71,
    6,
    "minecraft:iron_door[facing=west,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    71,
    7,
    "minecraft:iron_door[facing=north,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    71,
    8,
    "minecraft:iron_door[facing=north,half=upper,hinge=left,open=false,powered=false]"
  ],
  [
    71,
    9,
    "minecraft:iron_door[facing=north,half=upper,hinge=right,open=false,powered=false]"
  ],
  [
    71,
    10,
    "minecraft:iron_door[facing=north,half=upper,hinge=left,open=false,powered=true]"
  ],
  [
    71,
    11,
    "minecraft:iron_door[facing=north,half=upper,hinge=right,open=false,powered=true]"
  ],
  [72, 0, "minecraft:wooden_pressure_plate[powered=false]"],
  [72, 1, "minecraft:wooden_pressure_plate[powered=true]"],
  [73, 0, "minecraft:redstone_ore"],
  [74, 0, "minecraft:lit_redstone_ore"],
  [75, 0, "minecraft:unlit_redstone_torch[facing=up]"],
  [75, 1, "minecraft:unlit_redstone_torch[facing=east]"],
  [75, 2, "minecraft:unlit_redstone_torch[facing=west]"],
  [75, 3, "minecraft:unlit_redstone_torch[facing=south]"],
  [75, 4, "minecraft:unlit_redstone_torch[facing=north]"],
  [76, 0, "minecraft:redstone_torch[facing=up]"],
  [76, 1, "minecraft:redstone_torch[facing=east]"],
  [76, 2, "minecraft:redstone_torch[facing=west]"],
  [76, 3, "minecraft:redstone_torch[facing=south]"],
  [76, 4, "minecraft:redstone_torch[facing=north]"],
  [77, 0, "minecraft:stone_button[facing=down,powered=false]"],
  [77, 1, "minecraft:stone_button[facing=east,powered=false]"],
  [77, 2, "minecraft:stone_button[facing=west,powered=false]"],
  [77, 3, "minecraft:stone_button[facing=south,powered=false]"],
  [77, 4, "minecraft:stone_button[facing=north,powered=false]"],
  [77, 5, "minecraft:stone_button[facing=up,powered=false]"],
  [77, 8, "minecraft:stone_button[facing=down,powered=true]"],
  [77, 9, "minecraft:stone_button[facing=east,powered=true]"],
  [77, 10, "minecraft:stone_button[facing=west,powered=true]"],
  [77, 11, "minecraft:stone_button[facing=south,powered=true]"],
  [77, 12, "minecraft:stone_button[facing=north,powered=true]"],
  [77, 13, "minecraft:stone_button[facing=up,powered=true]"],
  [78, 0, "minecraft:snow_layer[layers=1]"],
  [78, 1, "minecraft:snow_layer[layers=2]"],
  [78, 2, "minecraft:snow_layer[layers=3]"],
  [78, 3, "minecraft:snow_layer[layers=4]"],
  [78, 4, "minecraft:snow_layer[layers=5]"],
  [78, 5, "minecraft:snow_layer[layers=6]"],
  [78, 6, "minecraft:snow_layer[layers=7]"],
  [78, 7, "minecraft:snow_layer[layers=8]"],
  [79, 0, "minecraft:ice"],
  [80, 0, "minecraft:snow"],
  [81, 0, "minecraft:cactus[age=0]"],
  [81, 1, "minecraft:cactus[age=1]"],
  [81, 2, "minecraft:cactus[age=2]"],
  [81, 3, "minecraft:cactus[age=3]"],
  [81, 4, "minecraft:cactus[age=4]"],
  [81, 5, "minecraft:cactus[age=5]"],
  [81, 6, "minecraft:cactus[age=6]"],
  [81, 7, "minecraft:cactus[age=7]"],
  [81, 8, "minecraft:cactus[age=8]"],
  [81, 9, "minecraft:cactus[age=9]"],
  [81, 10, "minecraft:cactus[age=10]"],
  [81, 11, "minecraft:cactus[age=11]"],
  [81, 12, "minecraft:cactus[age=12]"],
  [81, 13, "minecraft:cactus[age=13]"],
  [81, 14, "minecraft:cactus[age=14]"],
  [81, 15, "minecraft:cactus[age=15]"],
  [82, 0, "minecraft:clay"],
  [83, 0, "minecraft:reeds[age=0]"],
  [83, 1, "minecraft:reeds[age=1]"],
  [83, 2, "minecraft:reeds[age=2]"],
  [83, 3, "minecraft:reeds[age=3]"],
  [83, 4, "minecraft:reeds[age=4]"],
  [83, 5, "minecraft:reeds[age=5]"],
  [83, 6, "minecraft:reeds[age=6]"],
  [83, 7, "minecraft:reeds[age=7]"],
  [83, 8, "minecraft:reeds[age=8]"],
  [83, 9, "minecraft:reeds[age=9]"],
  [83, 10, "minecraft:reeds[age=10]"],
  [83, 11, "minecraft:reeds[age=11]"],
  [83, 12, "minecraft:reeds[age=12]"],
  [83, 13, "minecraft:reeds[age=13]"],
  [83, 14, "minecraft:reeds[age=14]"],
  [83, 15, "minecraft:reeds[age=15]"],
  [84, 0, "minecraft:jukebox[has_record=false]"],
  [84, 1, "minecraft:jukebox[has_record=true]"],
  [85, 0, "minecraft:fence[east=false,north=false,south=false,west=false]"],
  [86, 0, "minecraft:pumpkin[facing=south]"],
  [86, 1, "minecraft:pumpkin[facing=west]"],
  [86, 2, "minecraft:pumpkin[facing=north]"],
  [86, 3, "minecraft:pumpkin[facing=east]"],
  [87, 0, "minecraft:netherrack"],
  [88, 0, "minecraft:soul_sand"],
  [89, 0, "minecraft:glowstone"],
  [90, 0, "minecraft:portal[axis=x]"],
  [90, 2, "minecraft:portal[axis=z]"],
  [91, 0, "minecraft:lit_pumpkin[facing=south]"],
  [91, 1, "minecraft:lit_pumpkin[facing=west]"],
  [91, 2, "minecraft:lit_pumpkin[facing=north]"],
  [91, 3, "minecraft:lit_pumpkin[facing=east]"],
  [92, 0, "minecraft:cake[bites=0]"],
  [92, 1, "minecraft:cake[bites=1]"],
  [92, 2, "minecraft:cake[bites=2]"],
  [92, 3, "minecraft:cake[bites=3]"],
  [92, 4, "minecraft:cake[bites=4]"],
  [92, 5, "minecraft:cake[bites=5]"],
  [92, 6, "minecraft:cake[bites=6]"],
  [93, 0, "minecraft:unpowered_repeater[delay=1,facing=south,locked=false]"],
  [93, 1, "minecraft:unpowered_repeater[delay=1,facing=west,locked=false]"],
  [93, 2, "minecraft:unpowered_repeater[delay=1,facing=north,locked=false]"],
  [93, 3, "minecraft:unpowered_repeater[delay=1,facing=east,locked=false]"],
  [93, 4, "minecraft:unpowered_repeater[delay=2,facing=south,locked=false]"],
  [93, 5, "minecraft:unpowered_repeater[delay=2,facing=west,locked=false]"],
  [93, 6, "minecraft:unpowered_repeater[delay=2,facing=north,locked=false]"],
  [93, 7, "minecraft:unpowered_repeater[delay=2,facing=east,locked=false]"],
  [93, 8, "minecraft:unpowered_repeater[delay=3,facing=south,locked=false]"],
  [93, 9, "minecraft:unpowered_repeater[delay=3,facing=west,locked=false]"],
  [93, 10, "minecraft:unpowered_repeater[delay=3,facing=north,locked=false]"],
  [93, 11, "minecraft:unpowered_repeater[delay=3,facing=east,locked=false]"],
  [93, 12, "minecraft:unpowered_repeater[delay=4,facing=south,locked=false]"],
  [93, 13, "minecraft:unpowered_repeater[delay=4,facing=west,locked=false]"],
  [93, 14, "minecraft:unpowered_repeater[delay=4,facing=north,locked=false]"],
  [93, 15, "minecraft:unpowered_repeater[delay=4,facing=east,locked=false]"],
  [94, 0, "minecraft:powered_repeater[delay=1,facing=south,locked=false]"],
  [94, 1, "minecraft:powered_repeater[delay=1,facing=west,locked=false]"],
  [94, 2, "minecraft:powered_repeater[delay=1,facing=north,locked=false]"],
  [94, 3, "minecraft:powered_repeater[delay=1,facing=east,locked=false]"],
  [94, 4, "minecraft:powered_repeater[delay=2,facing=south,locked=false]"],
  [94, 5, "minecraft:powered_repeater[delay=2,facing=west,locked=false]"],
  [94, 6, "minecraft:powered_repeater[delay=2,facing=north,locked=false]"],
  [94, 7, "minecraft:powered_repeater[delay=2,facing=east,locked=false]"],
  [94, 8, "minecraft:powered_repeater[delay=3,facing=south,locked=false]"],
  [94, 9, "minecraft:powered_repeater[delay=3,facing=west,locked=false]"],
  [94, 10, "minecraft:powered_repeater[delay=3,facing=north,locked=false]"],
  [94, 11, "minecraft:powered_repeater[delay=3,facing=east,locked=false]"],
  [94, 12, "minecraft:powered_repeater[delay=4,facing=south,locked=false]"],
  [94, 13, "minecraft:powered_repeater[delay=4,facing=west,locked=false]"],
  [94, 14, "minecraft:powered_repeater[delay=4,facing=north,locked=false]"],
  [94, 15, "minecraft:powered_repeater[delay=4,facing=east,locked=false]"],
  [95, 0, "minecraft:stained_glass[color=white]"],
  [95, 1, "minecraft:stained_glass[color=orange]"],
  [95, 2, "minecraft:stained_glass[color=magenta]"],
  [95, 3, "minecraft:stained_glass[color=light_blue]"],
  [95, 4, "minecraft:stained_glass[color=yellow]"],
  [95, 5, "minecraft:stained_glass[color=lime]"],
  [95, 6, "minecraft:stained_glass[color=pink]"],
  [95, 7, "minecraft:stained_glass[color=gray]"],
  [95, 8, "minecraft:stained_glass[color=silver]"],
  [95, 9, "minecraft:stained_glass[color=cyan]"],
  [95, 10, "minecraft:stained_glass[color=purple]"],
  [95, 11, "minecraft:stained_glass[color=blue]"],
  [95, 12, "minecraft:stained_glass[color=brown]"],
  [95, 13, "minecraft:stained_glass[color=green]"],
  [95, 14, "minecraft:stained_glass[color=red]"],
  [95, 15, "minecraft:stained_glass[color=black]"],
  [96, 0, "minecraft:trapdoor[facing=north,half=bottom,open=false]"],
  [96, 1, "minecraft:trapdoor[facing=south,half=bottom,open=false]"],
  [96, 2, "minecraft:trapdoor[facing=west,half=bottom,open=false]"],
  [96, 3, "minecraft:trapdoor[facing=east,half=bottom,open=false]"],
  [96, 4, "minecraft:trapdoor[facing=north,half=bottom,open=true]"],
  [96, 5, "minecraft:trapdoor[facing=south,half=bottom,open=true]"],
  [96, 6, "minecraft:trapdoor[facing=west,half=bottom,open=true]"],
  [96, 7, "minecraft:trapdoor[facing=east,half=bottom,open=true]"],
  [96, 8, "minecraft:trapdoor[facing=north,half=top,open=false]"],
  [96, 9, "minecraft:trapdoor[facing=south,half=top,open=false]"],
  [96, 10, "minecraft:trapdoor[facing=west,half=top,open=false]"],
  [96, 11, "minecraft:trapdoor[facing=east,half=top,open=false]"],
  [96, 12, "minecraft:trapdoor[facing=north,half=top,open=true]"],
  [96, 13, "minecraft:trapdoor[facing=south,half=top,open=true]"],
  [96, 14, "minecraft:trapdoor[facing=west,half=top,open=true]"],
  [96, 15, "minecraft:trapdoor[facing=east,half=top,open=true]"],
  [97, 0, "minecraft:monster_egg[variant=stone]"],
  [97, 1, "minecraft:monster_egg[variant=cobblestone]"],
  [97, 2, "minecraft:monster_egg[variant=stone_brick]"],
  [97, 3, "minecraft:monster_egg[variant=mossy_brick]"],
  [97, 4, "minecraft:monster_egg[variant=cracked_brick]"],
  [97, 5, "minecraft:monster_egg[variant=chiseled_brick]"],
  [98, 0, "minecraft:stonebrick[variant=stonebrick]"],
  [98, 1, "minecraft:stonebrick[variant=mossy_stonebrick]"],
  [98, 2, "minecraft:stonebrick[variant=cracked_stonebrick]"],
  [98, 3, "minecraft:stonebrick[variant=chiseled_stonebrick]"],
  [99, 0, "minecraft:brown_mushroom_block[variant=all_inside]"],
  [99, 1, "minecraft:brown_mushroom_block[variant=north_west]"],
  [99, 2, "minecraft:brown_mushroom_block[variant=north]"],
  [99, 3, "minecraft:brown_mushroom_block[variant=north_east]"],
  [99, 4, "minecraft:brown_mushroom_block[variant=west]"],
  [99, 5, "minecraft:brown_mushroom_block[variant=center]"],
  [99, 6, "minecraft:brown_mushroom_block[variant=east]"],
  [99, 7, "minecraft:brown_mushroom_block[variant=south_west]"],
  [99, 8, "minecraft:brown_mushroom_block[variant=south]"],
  [99, 9, "minecraft:brown_mushroom_block[variant=south_east]"],
  [99, 10, "minecraft:brown_mushroom_block[variant=stem]"],
  [99, 14, "minecraft:brown_mushroom_block[variant=all_outside]"],
  [99, 15, "minecraft:brown_mushroom_block[variant=all_stem]"],
  [100, 0, "minecraft:red_mushroom_block[variant=all_inside]"],
  [100, 1, "minecraft:red_mushroom_block[variant=north_west]"],
  [100, 2, "minecraft:red_mushroom_block[variant=north]"],
  [100, 3, "minecraft:red_mushroom_block[variant=north_east]"],
  [100, 4, "minecraft:red_mushroom_block[variant=west]"],
  [100, 5, "minecraft:red_mushroom_block[variant=center]"],
  [100, 6, "minecraft:red_mushroom_block[variant=east]"],
  [100, 7, "minecraft:red_mushroom_block[variant=south_west]"],
  [100, 8, "minecraft:red_mushroom_block[variant=south]"],
  [100, 9, "minecraft:red_mushroom_block[variant=south_east]"],
  [100, 10, "minecraft:red_mushroom_block[variant=stem]"],
  [100, 14, "minecraft:red_mushroom_block[variant=all_outside]"],
  [100, 15, "minecraft:red_mushroom_block[variant=all_stem]"],
  [
    101,
    0,
    "minecraft:iron_bars[east=false,north=false,south=false,west=false]"
  ],
  [
    102,
    0,
    "minecraft:glass_pane[east=false,north=false,south=false,west=false]"
  ],
  [103, 0, "minecraft:melon_block"],
  [104, 0, "minecraft:pumpkin_stem[age=0,facing=up]"],
  [104, 1, "minecraft:pumpkin_stem[age=1,facing=up]"],
  [104, 2, "minecraft:pumpkin_stem[age=2,facing=up]"],
  [104, 3, "minecraft:pumpkin_stem[age=3,facing=up]"],
  [104, 4, "minecraft:pumpkin_stem[age=4,facing=up]"],
  [104, 5, "minecraft:pumpkin_stem[age=5,facing=up]"],
  [104, 6, "minecraft:pumpkin_stem[age=6,facing=up]"],
  [104, 7, "minecraft:pumpkin_stem[age=7,facing=up]"],
  [105, 0, "minecraft:melon_stem[age=0,facing=up]"],
  [105, 1, "minecraft:melon_stem[age=1,facing=up]"],
  [105, 2, "minecraft:melon_stem[age=2,facing=up]"],
  [105, 3, "minecraft:melon_stem[age=3,facing=up]"],
  [105, 4, "minecraft:melon_stem[age=4,facing=up]"],
  [105, 5, "minecraft:melon_stem[age=5,facing=up]"],
  [105, 6, "minecraft:melon_stem[age=6,facing=up]"],
  [105, 7, "minecraft:melon_stem[age=7,facing=up]"],
  [
    106,
    0,
    "minecraft:vine[east=false,north=false,south=false,up=false,west=false]"
  ],
  [
    106,
    1,
    "minecraft:vine[east=false,north=false,south=true,up=false,west=false]"
  ],
  [
    106,
    2,
    "minecraft:vine[east=false,north=false,south=false,up=false,west=true]"
  ],
  [
    106,
    3,
    "minecraft:vine[east=false,north=false,south=true,up=false,west=true]"
  ],
  [
    106,
    4,
    "minecraft:vine[east=false,north=true,south=false,up=false,west=false]"
  ],
  [
    106,
    5,
    "minecraft:vine[east=false,north=true,south=true,up=false,west=false]"
  ],
  [
    106,
    6,
    "minecraft:vine[east=false,north=true,south=false,up=false,west=true]"
  ],
  [
    106,
    7,
    "minecraft:vine[east=false,north=true,south=true,up=false,west=true]"
  ],
  [
    106,
    8,
    "minecraft:vine[east=true,north=false,south=false,up=false,west=false]"
  ],
  [
    106,
    9,
    "minecraft:vine[east=true,north=false,south=true,up=false,west=false]"
  ],
  [
    106,
    10,
    "minecraft:vine[east=true,north=false,south=false,up=false,west=true]"
  ],
  [
    106,
    11,
    "minecraft:vine[east=true,north=false,south=true,up=false,west=true]"
  ],
  [
    106,
    12,
    "minecraft:vine[east=true,north=true,south=false,up=false,west=false]"
  ],
  [
    106,
    13,
    "minecraft:vine[east=true,north=true,south=true,up=false,west=false]"
  ],
  [
    106,
    14,
    "minecraft:vine[east=true,north=true,south=false,up=false,west=true]"
  ],
  [
    106,
    15,
    "minecraft:vine[east=true,north=true,south=true,up=false,west=true]"
  ],
  [
    107,
    0,
    "minecraft:fence_gate[facing=south,in_wall=false,open=false,powered=false]"
  ],
  [
    107,
    1,
    "minecraft:fence_gate[facing=west,in_wall=false,open=false,powered=false]"
  ],
  [
    107,
    2,
    "minecraft:fence_gate[facing=north,in_wall=false,open=false,powered=false]"
  ],
  [
    107,
    3,
    "minecraft:fence_gate[facing=east,in_wall=false,open=false,powered=false]"
  ],
  [
    107,
    4,
    "minecraft:fence_gate[facing=south,in_wall=false,open=true,powered=false]"
  ],
  [
    107,
    5,
    "minecraft:fence_gate[facing=west,in_wall=false,open=true,powered=false]"
  ],
  [
    107,
    6,
    "minecraft:fence_gate[facing=north,in_wall=false,open=true,powered=false]"
  ],
  [
    107,
    7,
    "minecraft:fence_gate[facing=east,in_wall=false,open=true,powered=false]"
  ],
  [
    107,
    8,
    "minecraft:fence_gate[facing=south,in_wall=false,open=false,powered=true]"
  ],
  [
    107,
    9,
    "minecraft:fence_gate[facing=west,in_wall=false,open=false,powered=true]"
  ],
  [
    107,
    10,
    "minecraft:fence_gate[facing=north,in_wall=false,open=false,powered=true]"
  ],
  [
    107,
    11,
    "minecraft:fence_gate[facing=east,in_wall=false,open=false,powered=true]"
  ],
  [
    107,
    12,
    "minecraft:fence_gate[facing=south,in_wall=false,open=true,powered=true]"
  ],
  [
    107,
    13,
    "minecraft:fence_gate[facing=west,in_wall=false,open=true,powered=true]"
  ],
  [
    107,
    14,
    "minecraft:fence_gate[facing=north,in_wall=false,open=true,powered=true]"
  ],
  [
    107,
    15,
    "minecraft:fence_gate[facing=east,in_wall=false,open=true,powered=true]"
  ],
  [108, 0, "minecraft:brick_stairs[facing=east,half=bottom,shape=straight]"],
  [108, 1, "minecraft:brick_stairs[facing=west,half=bottom,shape=straight]"],
  [108, 2, "minecraft:brick_stairs[facing=south,half=bottom,shape=straight]"],
  [108, 3, "minecraft:brick_stairs[facing=north,half=bottom,shape=straight]"],
  [108, 4, "minecraft:brick_stairs[facing=east,half=top,shape=straight]"],
  [108, 5, "minecraft:brick_stairs[facing=west,half=top,shape=straight]"],
  [108, 6, "minecraft:brick_stairs[facing=south,half=top,shape=straight]"],
  [108, 7, "minecraft:brick_stairs[facing=north,half=top,shape=straight]"],
  [
    109,
    0,
    "minecraft:stone_brick_stairs[facing=east,half=bottom,shape=straight]"
  ],
  [
    109,
    1,
    "minecraft:stone_brick_stairs[facing=west,half=bottom,shape=straight]"
  ],
  [
    109,
    2,
    "minecraft:stone_brick_stairs[facing=south,half=bottom,shape=straight]"
  ],
  [
    109,
    3,
    "minecraft:stone_brick_stairs[facing=north,half=bottom,shape=straight]"
  ],
  [109, 4, "minecraft:stone_brick_stairs[facing=east,half=top,shape=straight]"],
  [109, 5, "minecraft:stone_brick_stairs[facing=west,half=top,shape=straight]"],
  [
    109,
    6,
    "minecraft:stone_brick_stairs[facing=south,half=top,shape=straight]"
  ],
  [
    109,
    7,
    "minecraft:stone_brick_stairs[facing=north,half=top,shape=straight]"
  ],
  [110, 0, "minecraft:mycelium[snowy=false]"],
  [111, 0, "minecraft:waterlily"],
  [112, 0, "minecraft:nether_brick"],
  [
    113,
    0,
    "minecraft:nether_brick_fence[east=false,north=false,south=false,west=false]"
  ],
  [
    114,
    0,
    "minecraft:nether_brick_stairs[facing=east,half=bottom,shape=straight]"
  ],
  [
    114,
    1,
    "minecraft:nether_brick_stairs[facing=west,half=bottom,shape=straight]"
  ],
  [
    114,
    2,
    "minecraft:nether_brick_stairs[facing=south,half=bottom,shape=straight]"
  ],
  [
    114,
    3,
    "minecraft:nether_brick_stairs[facing=north,half=bottom,shape=straight]"
  ],
  [
    114,
    4,
    "minecraft:nether_brick_stairs[facing=east,half=top,shape=straight]"
  ],
  [
    114,
    5,
    "minecraft:nether_brick_stairs[facing=west,half=top,shape=straight]"
  ],
  [
    114,
    6,
    "minecraft:nether_brick_stairs[facing=south,half=top,shape=straight]"
  ],
  [
    114,
    7,
    "minecraft:nether_brick_stairs[facing=north,half=top,shape=straight]"
  ],
  [115, 0, "minecraft:nether_wart[age=0]"],
  [115, 1, "minecraft:nether_wart[age=1]"],
  [115, 2, "minecraft:nether_wart[age=2]"],
  [115, 3, "minecraft:nether_wart[age=3]"],
  [116, 0, "minecraft:enchanting_table"],
  [
    117,
    0,
    "minecraft:brewing_stand[has_bottle_0=false,has_bottle_1=false,has_bottle_2=false]"
  ],
  [
    117,
    1,
    "minecraft:brewing_stand[has_bottle_0=true,has_bottle_1=false,has_bottle_2=false]"
  ],
  [
    117,
    2,
    "minecraft:brewing_stand[has_bottle_0=false,has_bottle_1=true,has_bottle_2=false]"
  ],
  [
    117,
    3,
    "minecraft:brewing_stand[has_bottle_0=true,has_bottle_1=true,has_bottle_2=false]"
  ],
  [
    117,
    4,
    "minecraft:brewing_stand[has_bottle_0=false,has_bottle_1=false,has_bottle_2=true]"
  ],
  [
    117,
    5,
    "minecraft:brewing_stand[has_bottle_0=true,has_bottle_1=false,has_bottle_2=true]"
  ],
  [
    117,
    6,
    "minecraft:brewing_stand[has_bottle_0=false,has_bottle_1=true,has_bottle_2=true]"
  ],
  [
    117,
    7,
    "minecraft:brewing_stand[has_bottle_0=true,has_bottle_1=true,has_bottle_2=true]"
  ],
  [118, 0, "minecraft:cauldron[level=0]"],
  [118, 1, "minecraft:cauldron[level=1]"],
  [118, 2, "minecraft:cauldron[level=2]"],
  [118, 3, "minecraft:cauldron[level=3]"],
  [119, 0, "minecraft:end_portal"],
  [120, 0, "minecraft:end_portal_frame[eye=false,facing=south]"],
  [120, 1, "minecraft:end_portal_frame[eye=false,facing=west]"],
  [120, 2, "minecraft:end_portal_frame[eye=false,facing=north]"],
  [120, 3, "minecraft:end_portal_frame[eye=false,facing=east]"],
  [120, 4, "minecraft:end_portal_frame[eye=true,facing=south]"],
  [120, 5, "minecraft:end_portal_frame[eye=true,facing=west]"],
  [120, 6, "minecraft:end_portal_frame[eye=true,facing=north]"],
  [120, 7, "minecraft:end_portal_frame[eye=true,facing=east]"],
  [121, 0, "minecraft:end_stone"],
  [122, 0, "minecraft:dragon_egg"],
  [123, 0, "minecraft:redstone_lamp"],
  [124, 0, "minecraft:lit_redstone_lamp"],
  [125, 0, "minecraft:double_wooden_slab[variant=oak]"],
  [125, 1, "minecraft:double_wooden_slab[variant=spruce]"],
  [125, 2, "minecraft:double_wooden_slab[variant=birch]"],
  [125, 3, "minecraft:double_wooden_slab[variant=jungle]"],
  [125, 4, "minecraft:double_wooden_slab[variant=acacia]"],
  [125, 5, "minecraft:double_wooden_slab[variant=dark_oak]"],
  [126, 0, "minecraft:wooden_slab[half=bottom,variant=oak]"],
  [126, 1, "minecraft:wooden_slab[half=bottom,variant=spruce]"],
  [126, 2, "minecraft:wooden_slab[half=bottom,variant=birch]"],
  [126, 3, "minecraft:wooden_slab[half=bottom,variant=jungle]"],
  [126, 4, "minecraft:wooden_slab[half=bottom,variant=acacia]"],
  [126, 5, "minecraft:wooden_slab[half=bottom,variant=dark_oak]"],
  [126, 8, "minecraft:wooden_slab[half=top,variant=oak]"],
  [126, 9, "minecraft:wooden_slab[half=top,variant=spruce]"],
  [126, 10, "minecraft:wooden_slab[half=top,variant=birch]"],
  [126, 11, "minecraft:wooden_slab[half=top,variant=jungle]"],
  [126, 12, "minecraft:wooden_slab[half=top,variant=acacia]"],
  [126, 13, "minecraft:wooden_slab[half=top,variant=dark_oak]"],
  [127, 0, "minecraft:cocoa[age=0,facing=south]"],
  [127, 1, "minecraft:cocoa[age=0,facing=west]"],
  [127, 2, "minecraft:cocoa[age=0,facing=north]"],
  [127, 3, "minecraft:cocoa[age=0,facing=east]"],
  [127, 4, "minecraft:cocoa[age=1,facing=south]"],
  [127, 5, "minecraft:cocoa[age=1,facing=west]"],
  [127, 6, "minecraft:cocoa[age=1,facing=north]"],
  [127, 7, "minecraft:cocoa[age=1,facing=east]"],
  [127, 8, "minecraft:cocoa[age=2,facing=south]"],
  [127, 9, "minecraft:cocoa[age=2,facing=west]"],
  [127, 10, "minecraft:cocoa[age=2,facing=north]"],
  [127, 11, "minecraft:cocoa[age=2,facing=east]"],
  [
    128,
    0,
    "minecraft:sandstone_stairs[facing=east,half=bottom,shape=straight]"
  ],
  [
    128,
    1,
    "minecraft:sandstone_stairs[facing=west,half=bottom,shape=straight]"
  ],
  [
    128,
    2,
    "minecraft:sandstone_stairs[facing=south,half=bottom,shape=straight]"
  ],
  [
    128,
    3,
    "minecraft:sandstone_stairs[facing=north,half=bottom,shape=straight]"
  ],
  [128, 4, "minecraft:sandstone_stairs[facing=east,half=top,shape=straight]"],
  [128, 5, "minecraft:sandstone_stairs[facing=west,half=top,shape=straight]"],
  [128, 6, "minecraft:sandstone_stairs[facing=south,half=top,shape=straight]"],
  [128, 7, "minecraft:sandstone_stairs[facing=north,half=top,shape=straight]"],
  [129, 0, "minecraft:emerald_ore"],
  [130, 0, "minecraft:ender_chest[facing=north]"],
  [130, 3, "minecraft:ender_chest[facing=south]"],
  [130, 4, "minecraft:ender_chest[facing=west]"],
  [130, 5, "minecraft:ender_chest[facing=east]"],
  [
    131,
    0,
    "minecraft:tripwire_hook[attached=false,facing=south,powered=false]"
  ],
  [131, 1, "minecraft:tripwire_hook[attached=false,facing=west,powered=false]"],
  [
    131,
    2,
    "minecraft:tripwire_hook[attached=false,facing=north,powered=false]"
  ],
  [131, 3, "minecraft:tripwire_hook[attached=false,facing=east,powered=false]"],
  [131, 4, "minecraft:tripwire_hook[attached=true,facing=south,powered=false]"],
  [131, 5, "minecraft:tripwire_hook[attached=true,facing=west,powered=false]"],
  [131, 6, "minecraft:tripwire_hook[attached=true,facing=north,powered=false]"],
  [131, 7, "minecraft:tripwire_hook[attached=true,facing=east,powered=false]"],
  [131, 8, "minecraft:tripwire_hook[attached=false,facing=south,powered=true]"],
  [131, 9, "minecraft:tripwire_hook[attached=false,facing=west,powered=true]"],
  [
    131,
    10,
    "minecraft:tripwire_hook[attached=false,facing=north,powered=true]"
  ],
  [131, 11, "minecraft:tripwire_hook[attached=false,facing=east,powered=true]"],
  [131, 12, "minecraft:tripwire_hook[attached=true,facing=south,powered=true]"],
  [131, 13, "minecraft:tripwire_hook[attached=true,facing=west,powered=true]"],
  [131, 14, "minecraft:tripwire_hook[attached=true,facing=north,powered=true]"],
  [131, 15, "minecraft:tripwire_hook[attached=true,facing=east,powered=true]"],
  [
    132,
    0,
    "minecraft:tripwire[attached=false,disarmed=false,east=false,north=false,powered=false,south=false,west=false]"
  ],
  [
    132,
    1,
    "minecraft:tripwire[attached=false,disarmed=false,east=false,north=false,powered=true,south=false,west=false]"
  ],
  [
    132,
    4,
    "minecraft:tripwire[attached=true,disarmed=false,east=false,north=false,powered=false,south=false,west=false]"
  ],
  [
    132,
    5,
    "minecraft:tripwire[attached=true,disarmed=false,east=false,north=false,powered=true,south=false,west=false]"
  ],
  [
    132,
    8,
    "minecraft:tripwire[attached=false,disarmed=true,east=false,north=false,powered=false,south=false,west=false]"
  ],
  [
    132,
    9,
    "minecraft:tripwire[attached=false,disarmed=true,east=false,north=false,powered=true,south=false,west=false]"
  ],
  [
    132,
    12,
    "minecraft:tripwire[attached=true,disarmed=true,east=false,north=false,powered=false,south=false,west=false]"
  ],
  [
    132,
    13,
    "minecraft:tripwire[attached=true,disarmed=true,east=false,north=false,powered=true,south=false,west=false]"
  ],
  [133, 0, "minecraft:emerald_block"],
  [134, 0, "minecraft:spruce_stairs[facing=east,half=bottom,shape=straight]"],
  [134, 1, "minecraft:spruce_stairs[facing=west,half=bottom,shape=straight]"],
  [134, 2, "minecraft:spruce_stairs[facing=south,half=bottom,shape=straight]"],
  [134, 3, "minecraft:spruce_stairs[facing=north,half=bottom,shape=straight]"],
  [134, 4, "minecraft:spruce_stairs[facing=east,half=top,shape=straight]"],
  [134, 5, "minecraft:spruce_stairs[facing=west,half=top,shape=straight]"],
  [134, 6, "minecraft:spruce_stairs[facing=south,half=top,shape=straight]"],
  [134, 7, "minecraft:spruce_stairs[facing=north,half=top,shape=straight]"],
  [135, 0, "minecraft:birch_stairs[facing=east,half=bottom,shape=straight]"],
  [135, 1, "minecraft:birch_stairs[facing=west,half=bottom,shape=straight]"],
  [135, 2, "minecraft:birch_stairs[facing=south,half=bottom,shape=straight]"],
  [135, 3, "minecraft:birch_stairs[facing=north,half=bottom,shape=straight]"],
  [135, 4, "minecraft:birch_stairs[facing=east,half=top,shape=straight]"],
  [135, 5, "minecraft:birch_stairs[facing=west,half=top,shape=straight]"],
  [135, 6, "minecraft:birch_stairs[facing=south,half=top,shape=straight]"],
  [135, 7, "minecraft:birch_stairs[facing=north,half=top,shape=straight]"],
  [136, 0, "minecraft:jungle_stairs[facing=east,half=bottom,shape=straight]"],
  [136, 1, "minecraft:jungle_stairs[facing=west,half=bottom,shape=straight]"],
  [136, 2, "minecraft:jungle_stairs[facing=south,half=bottom,shape=straight]"],
  [136, 3, "minecraft:jungle_stairs[facing=north,half=bottom,shape=straight]"],
  [136, 4, "minecraft:jungle_stairs[facing=east,half=top,shape=straight]"],
  [136, 5, "minecraft:jungle_stairs[facing=west,half=top,shape=straight]"],
  [136, 6, "minecraft:jungle_stairs[facing=south,half=top,shape=straight]"],
  [136, 7, "minecraft:jungle_stairs[facing=north,half=top,shape=straight]"],
  [137, 0, "minecraft:command_block[conditional=false,facing=down]"],
  [137, 1, "minecraft:command_block[conditional=false,facing=up]"],
  [137, 2, "minecraft:command_block[conditional=false,facing=north]"],
  [137, 3, "minecraft:command_block[conditional=false,facing=south]"],
  [137, 4, "minecraft:command_block[conditional=false,facing=west]"],
  [137, 5, "minecraft:command_block[conditional=false,facing=east]"],
  [137, 8, "minecraft:command_block[conditional=true,facing=down]"],
  [137, 9, "minecraft:command_block[conditional=true,facing=up]"],
  [137, 10, "minecraft:command_block[conditional=true,facing=north]"],
  [137, 11, "minecraft:command_block[conditional=true,facing=south]"],
  [137, 12, "minecraft:command_block[conditional=true,facing=west]"],
  [137, 13, "minecraft:command_block[conditional=true,facing=east]"],
  [138, 0, "minecraft:beacon"],
  [
    139,
    0,
    "minecraft:cobblestone_wall[east=false,north=false,south=false,up=false,variant=cobblestone,west=false]"
  ],
  [
    139,
    1,
    "minecraft:cobblestone_wall[east=false,north=false,south=false,up=false,variant=mossy_cobblestone,west=false]"
  ],
  [140, 0, "minecraft:flower_pot[contents=empty,legacy_data=0]"],
  [141, 0, "minecraft:carrots[age=0]"],
  [141, 1, "minecraft:carrots[age=1]"],
  [141, 2, "minecraft:carrots[age=2]"],
  [141, 3, "minecraft:carrots[age=3]"],
  [141, 4, "minecraft:carrots[age=4]"],
  [141, 5, "minecraft:carrots[age=5]"],
  [141, 6, "minecraft:carrots[age=6]"],
  [141, 7, "minecraft:carrots[age=7]"],
  [142, 0, "minecraft:potatoes[age=0]"],
  [142, 1, "minecraft:potatoes[age=1]"],
  [142, 2, "minecraft:potatoes[age=2]"],
  [142, 3, "minecraft:potatoes[age=3]"],
  [142, 4, "minecraft:potatoes[age=4]"],
  [142, 5, "minecraft:potatoes[age=5]"],
  [142, 6, "minecraft:potatoes[age=6]"],
  [142, 7, "minecraft:potatoes[age=7]"],
  [143, 0, "minecraft:wooden_button[facing=down,powered=false]"],
  [143, 1, "minecraft:wooden_button[facing=east,powered=false]"],
  [143, 2, "minecraft:wooden_button[facing=west,powered=false]"],
  [143, 3, "minecraft:wooden_button[facing=south,powered=false]"],
  [143, 4, "minecraft:wooden_button[facing=north,powered=false]"],
  [143, 5, "minecraft:wooden_button[facing=up,powered=false]"],
  [143, 8, "minecraft:wooden_button[facing=down,powered=true]"],
  [143, 9, "minecraft:wooden_button[facing=east,powered=true]"],
  [143, 10, "minecraft:wooden_button[facing=west,powered=true]"],
  [143, 11, "minecraft:wooden_button[facing=south,powered=true]"],
  [143, 12, "minecraft:wooden_button[facing=north,powered=true]"],
  [143, 13, "minecraft:wooden_button[facing=up,powered=true]"],
  [144, 0, "minecraft:skull[facing=down,nodrop=false]"],
  [144, 1, "minecraft:skull[facing=up,nodrop=false]"],
  [144, 2, "minecraft:skull[facing=north,nodrop=false]"],
  [144, 3, "minecraft:skull[facing=south,nodrop=false]"],
  [144, 4, "minecraft:skull[facing=west,nodrop=false]"],
  [144, 5, "minecraft:skull[facing=east,nodrop=false]"],
  [144, 8, "minecraft:skull[facing=down,nodrop=true]"],
  [144, 9, "minecraft:skull[facing=up,nodrop=true]"],
  [144, 10, "minecraft:skull[facing=north,nodrop=true]"],
  [144, 11, "minecraft:skull[facing=south,nodrop=true]"],
  [144, 12, "minecraft:skull[facing=west,nodrop=true]"],
  [144, 13, "minecraft:skull[facing=east,nodrop=true]"],
  [145, 0, "minecraft:anvil[damage=0,facing=south]"],
  [145, 1, "minecraft:anvil[damage=0,facing=west]"],
  [145, 2, "minecraft:anvil[damage=0,facing=north]"],
  [145, 3, "minecraft:anvil[damage=0,facing=east]"],
  [145, 4, "minecraft:anvil[damage=1,facing=south]"],
  [145, 5, "minecraft:anvil[damage=1,facing=west]"],
  [145, 6, "minecraft:anvil[damage=1,facing=north]"],
  [145, 7, "minecraft:anvil[damage=1,facing=east]"],
  [145, 8, "minecraft:anvil[damage=2,facing=south]"],
  [145, 9, "minecraft:anvil[damage=2,facing=west]"],
  [145, 10, "minecraft:anvil[damage=2,facing=north]"],
  [145, 11, "minecraft:anvil[damage=2,facing=east]"],
  [146, 0, "minecraft:trapped_chest[facing=north]"],
  [146, 3, "minecraft:trapped_chest[facing=south]"],
  [146, 4, "minecraft:trapped_chest[facing=west]"],
  [146, 5, "minecraft:trapped_chest[facing=east]"],
  [147, 0, "minecraft:light_weighted_pressure_plate[power=0]"],
  [147, 1, "minecraft:light_weighted_pressure_plate[power=1]"],
  [147, 2, "minecraft:light_weighted_pressure_plate[power=2]"],
  [147, 3, "minecraft:light_weighted_pressure_plate[power=3]"],
  [147, 4, "minecraft:light_weighted_pressure_plate[power=4]"],
  [147, 5, "minecraft:light_weighted_pressure_plate[power=5]"],
  [147, 6, "minecraft:light_weighted_pressure_plate[power=6]"],
  [147, 7, "minecraft:light_weighted_pressure_plate[power=7]"],
  [147, 8, "minecraft:light_weighted_pressure_plate[power=8]"],
  [147, 9, "minecraft:light_weighted_pressure_plate[power=9]"],
  [147, 10, "minecraft:light_weighted_pressure_plate[power=10]"],
  [147, 11, "minecraft:light_weighted_pressure_plate[power=11]"],
  [147, 12, "minecraft:light_weighted_pressure_plate[power=12]"],
  [147, 13, "minecraft:light_weighted_pressure_plate[power=13]"],
  [147, 14, "minecraft:light_weighted_pressure_plate[power=14]"],
  [147, 15, "minecraft:light_weighted_pressure_plate[power=15]"],
  [148, 0, "minecraft:heavy_weighted_pressure_plate[power=0]"],
  [148, 1, "minecraft:heavy_weighted_pressure_plate[power=1]"],
  [148, 2, "minecraft:heavy_weighted_pressure_plate[power=2]"],
  [148, 3, "minecraft:heavy_weighted_pressure_plate[power=3]"],
  [148, 4, "minecraft:heavy_weighted_pressure_plate[power=4]"],
  [148, 5, "minecraft:heavy_weighted_pressure_plate[power=5]"],
  [148, 6, "minecraft:heavy_weighted_pressure_plate[power=6]"],
  [148, 7, "minecraft:heavy_weighted_pressure_plate[power=7]"],
  [148, 8, "minecraft:heavy_weighted_pressure_plate[power=8]"],
  [148, 9, "minecraft:heavy_weighted_pressure_plate[power=9]"],
  [148, 10, "minecraft:heavy_weighted_pressure_plate[power=10]"],
  [148, 11, "minecraft:heavy_weighted_pressure_plate[power=11]"],
  [148, 12, "minecraft:heavy_weighted_pressure_plate[power=12]"],
  [148, 13, "minecraft:heavy_weighted_pressure_plate[power=13]"],
  [148, 14, "minecraft:heavy_weighted_pressure_plate[power=14]"],
  [148, 15, "minecraft:heavy_weighted_pressure_plate[power=15]"],
  [
    149,
    0,
    "minecraft:unpowered_comparator[facing=south,mode=compare,powered=false]"
  ],
  [
    149,
    1,
    "minecraft:unpowered_comparator[facing=west,mode=compare,powered=false]"
  ],
  [
    149,
    2,
    "minecraft:unpowered_comparator[facing=north,mode=compare,powered=false]"
  ],
  [
    149,
    3,
    "minecraft:unpowered_comparator[facing=east,mode=compare,powered=false]"
  ],
  [
    149,
    4,
    "minecraft:unpowered_comparator[facing=south,mode=subtract,powered=false]"
  ],
  [
    149,
    5,
    "minecraft:unpowered_comparator[facing=west,mode=subtract,powered=false]"
  ],
  [
    149,
    6,
    "minecraft:unpowered_comparator[facing=north,mode=subtract,powered=false]"
  ],
  [
    149,
    7,
    "minecraft:unpowered_comparator[facing=east,mode=subtract,powered=false]"
  ],
  [
    149,
    8,
    "minecraft:unpowered_comparator[facing=south,mode=compare,powered=true]"
  ],
  [
    149,
    9,
    "minecraft:unpowered_comparator[facing=west,mode=compare,powered=true]"
  ],
  [
    149,
    10,
    "minecraft:unpowered_comparator[facing=north,mode=compare,powered=true]"
  ],
  [
    149,
    11,
    "minecraft:unpowered_comparator[facing=east,mode=compare,powered=true]"
  ],
  [
    149,
    12,
    "minecraft:unpowered_comparator[facing=south,mode=subtract,powered=true]"
  ],
  [
    149,
    13,
    "minecraft:unpowered_comparator[facing=west,mode=subtract,powered=true]"
  ],
  [
    149,
    14,
    "minecraft:unpowered_comparator[facing=north,mode=subtract,powered=true]"
  ],
  [
    149,
    15,
    "minecraft:unpowered_comparator[facing=east,mode=subtract,powered=true]"
  ],
  [
    150,
    0,
    "minecraft:powered_comparator[facing=south,mode=compare,powered=false]"
  ],
  [
    150,
    1,
    "minecraft:powered_comparator[facing=west,mode=compare,powered=false]"
  ],
  [
    150,
    2,
    "minecraft:powered_comparator[facing=north,mode=compare,powered=false]"
  ],
  [
    150,
    3,
    "minecraft:powered_comparator[facing=east,mode=compare,powered=false]"
  ],
  [
    150,
    4,
    "minecraft:powered_comparator[facing=south,mode=subtract,powered=false]"
  ],
  [
    150,
    5,
    "minecraft:powered_comparator[facing=west,mode=subtract,powered=false]"
  ],
  [
    150,
    6,
    "minecraft:powered_comparator[facing=north,mode=subtract,powered=false]"
  ],
  [
    150,
    7,
    "minecraft:powered_comparator[facing=east,mode=subtract,powered=false]"
  ],
  [
    150,
    8,
    "minecraft:powered_comparator[facing=south,mode=compare,powered=true]"
  ],
  [
    150,
    9,
    "minecraft:powered_comparator[facing=west,mode=compare,powered=true]"
  ],
  [
    150,
    10,
    "minecraft:powered_comparator[facing=north,mode=compare,powered=true]"
  ],
  [
    150,
    11,
    "minecraft:powered_comparator[facing=east,mode=compare,powered=true]"
  ],
  [
    150,
    12,
    "minecraft:powered_comparator[facing=south,mode=subtract,powered=true]"
  ],
  [
    150,
    13,
    "minecraft:powered_comparator[facing=west,mode=subtract,powered=true]"
  ],
  [
    150,
    14,
    "minecraft:powered_comparator[facing=north,mode=subtract,powered=true]"
  ],
  [
    150,
    15,
    "minecraft:powered_comparator[facing=east,mode=subtract,powered=true]"
  ],
  [151, 0, "minecraft:daylight_detector[power=0]"],
  [151, 1, "minecraft:daylight_detector[power=1]"],
  [151, 2, "minecraft:daylight_detector[power=2]"],
  [151, 3, "minecraft:daylight_detector[power=3]"],
  [151, 4, "minecraft:daylight_detector[power=4]"],
  [151, 5, "minecraft:daylight_detector[power=5]"],
  [151, 6, "minecraft:daylight_detector[power=6]"],
  [151, 7, "minecraft:daylight_detector[power=7]"],
  [151, 8, "minecraft:daylight_detector[power=8]"],
  [151, 9, "minecraft:daylight_detector[power=9]"],
  [151, 10, "minecraft:daylight_detector[power=10]"],
  [151, 11, "minecraft:daylight_detector[power=11]"],
  [151, 12, "minecraft:daylight_detector[power=12]"],
  [151, 13, "minecraft:daylight_detector[power=13]"],
  [151, 14, "minecraft:daylight_detector[power=14]"],
  [151, 15, "minecraft:daylight_detector[power=15]"],
  [152, 0, "minecraft:redstone_block"],
  [153, 0, "minecraft:quartz_ore"],
  [154, 0, "minecraft:hopper[enabled=true,facing=down]"],
  [154, 2, "minecraft:hopper[enabled=true,facing=north]"],
  [154, 3, "minecraft:hopper[enabled=true,facing=south]"],
  [154, 4, "minecraft:hopper[enabled=true,facing=west]"],
  [154, 5, "minecraft:hopper[enabled=true,facing=east]"],
  [154, 8, "minecraft:hopper[enabled=false,facing=down]"],
  [154, 10, "minecraft:hopper[enabled=false,facing=north]"],
  [154, 11, "minecraft:hopper[enabled=false,facing=south]"],
  [154, 12, "minecraft:hopper[enabled=false,facing=west]"],
  [154, 13, "minecraft:hopper[enabled=false,facing=east]"],
  [155, 0, "minecraft:quartz_block[variant=default]"],
  [155, 1, "minecraft:quartz_block[variant=chiseled]"],
  [155, 2, "minecraft:quartz_block[variant=lines_y]"],
  [155, 3, "minecraft:quartz_block[variant=lines_x]"],
  [155, 4, "minecraft:quartz_block[variant=lines_z]"],
  [156, 0, "minecraft:quartz_stairs[facing=east,half=bottom,shape=straight]"],
  [156, 1, "minecraft:quartz_stairs[facing=west,half=bottom,shape=straight]"],
  [156, 2, "minecraft:quartz_stairs[facing=south,half=bottom,shape=straight]"],
  [156, 3, "minecraft:quartz_stairs[facing=north,half=bottom,shape=straight]"],
  [156, 4, "minecraft:quartz_stairs[facing=east,half=top,shape=straight]"],
  [156, 5, "minecraft:quartz_stairs[facing=west,half=top,shape=straight]"],
  [156, 6, "minecraft:quartz_stairs[facing=south,half=top,shape=straight]"],
  [156, 7, "minecraft:quartz_stairs[facing=north,half=top,shape=straight]"],
  [157, 0, "minecraft:activator_rail[powered=false,shape=north_south]"],
  [157, 1, "minecraft:activator_rail[powered=false,shape=east_west]"],
  [157, 2, "minecraft:activator_rail[powered=false,shape=ascending_east]"],
  [157, 3, "minecraft:activator_rail[powered=false,shape=ascending_west]"],
  [157, 4, "minecraft:activator_rail[powered=false,shape=ascending_north]"],
  [157, 5, "minecraft:activator_rail[powered=false,shape=ascending_south]"],
  [157, 8, "minecraft:activator_rail[powered=true,shape=north_south]"],
  [157, 9, "minecraft:activator_rail[powered=true,shape=east_west]"],
  [157, 10, "minecraft:activator_rail[powered=true,shape=ascending_east]"],
  [157, 11, "minecraft:activator_rail[powered=true,shape=ascending_west]"],
  [157, 12, "minecraft:activator_rail[powered=true,shape=ascending_north]"],
  [157, 13, "minecraft:activator_rail[powered=true,shape=ascending_south]"],
  [158, 0, "minecraft:dropper[facing=down,triggered=false]"],
  [158, 1, "minecraft:dropper[facing=up,triggered=false]"],
  [158, 2, "minecraft:dropper[facing=north,triggered=false]"],
  [158, 3, "minecraft:dropper[facing=south,triggered=false]"],
  [158, 4, "minecraft:dropper[facing=west,triggered=false]"],
  [158, 5, "minecraft:dropper[facing=east,triggered=false]"],
  [158, 8, "minecraft:dropper[facing=down,triggered=true]"],
  [158, 9, "minecraft:dropper[facing=up,triggered=true]"],
  [158, 10, "minecraft:dropper[facing=north,triggered=true]"],
  [158, 11, "minecraft:dropper[facing=south,triggered=true]"],
  [158, 12, "minecraft:dropper[facing=west,triggered=true]"],
  [158, 13, "minecraft:dropper[facing=east,triggered=true]"],
  [159, 0, "minecraft:stained_hardened_clay[color=white]"],
  [159, 1, "minecraft:stained_hardened_clay[color=orange]"],
  [159, 2, "minecraft:stained_hardened_clay[color=magenta]"],
  [159, 3, "minecraft:stained_hardened_clay[color=light_blue]"],
  [159, 4, "minecraft:stained_hardened_clay[color=yellow]"],
  [159, 5, "minecraft:stained_hardened_clay[color=lime]"],
  [159, 6, "minecraft:stained_hardened_clay[color=pink]"],
  [159, 7, "minecraft:stained_hardened_clay[color=gray]"],
  [159, 8, "minecraft:stained_hardened_clay[color=silver]"],
  [159, 9, "minecraft:stained_hardened_clay[color=cyan]"],
  [159, 10, "minecraft:stained_hardened_clay[color=purple]"],
  [159, 11, "minecraft:stained_hardened_clay[color=blue]"],
  [159, 12, "minecraft:stained_hardened_clay[color=brown]"],
  [159, 13, "minecraft:stained_hardened_clay[color=green]"],
  [159, 14, "minecraft:stained_hardened_clay[color=red]"],
  [159, 15, "minecraft:stained_hardened_clay[color=black]"],
  [
    160,
    0,
    "minecraft:stained_glass_pane[color=white,east=false,north=false,south=false,west=false]"
  ],
  [
    160,
    1,
    "minecraft:stained_glass_pane[color=orange,east=false,north=false,south=false,west=false]"
  ],
  [
    160,
    2,
    "minecraft:stained_glass_pane[color=magenta,east=false,north=false,south=false,west=false]"
  ],
  [
    160,
    3,
    "minecraft:stained_glass_pane[color=light_blue,east=false,north=false,south=false,west=false]"
  ],
  [
    160,
    4,
    "minecraft:stained_glass_pane[color=yellow,east=false,north=false,south=false,west=false]"
  ],
  [
    160,
    5,
    "minecraft:stained_glass_pane[color=lime,east=false,north=false,south=false,west=false]"
  ],
  [
    160,
    6,
    "minecraft:stained_glass_pane[color=pink,east=false,north=false,south=false,west=false]"
  ],
  [
    160,
    7,
    "minecraft:stained_glass_pane[color=gray,east=false,north=false,south=false,west=false]"
  ],
  [
    160,
    8,
    "minecraft:stained_glass_pane[color=silver,east=false,north=false,south=false,west=false]"
  ],
  [
    160,
    9,
    "minecraft:stained_glass_pane[color=cyan,east=false,north=false,south=false,west=false]"
  ],
  [
    160,
    10,
    "minecraft:stained_glass_pane[color=purple,east=false,north=false,south=false,west=false]"
  ],
  [
    160,
    11,
    "minecraft:stained_glass_pane[color=blue,east=false,north=false,south=false,west=false]"
  ],
  [
    160,
    12,
    "minecraft:stained_glass_pane[color=brown,east=false,north=false,south=false,west=false]"
  ],
  [
    160,
    13,
    "minecraft:stained_glass_pane[color=green,east=false,north=false,south=false,west=false]"
  ],
  [
    160,
    14,
    "minecraft:stained_glass_pane[color=red,east=false,north=false,south=false,west=false]"
  ],
  [
    160,
    15,
    "minecraft:stained_glass_pane[color=black,east=false,north=false,south=false,west=false]"
  ],
  [
    161,
    0,
    "minecraft:leaves2[check_decay=false,decayable=true,variant=acacia]"
  ],
  [
    161,
    1,
    "minecraft:leaves2[check_decay=false,decayable=true,variant=dark_oak]"
  ],
  [
    161,
    4,
    "minecraft:leaves2[check_decay=false,decayable=false,variant=acacia]"
  ],
  [
    161,
    5,
    "minecraft:leaves2[check_decay=false,decayable=false,variant=dark_oak]"
  ],
  [161, 8, "minecraft:leaves2[check_decay=true,decayable=true,variant=acacia]"],
  [
    161,
    9,
    "minecraft:leaves2[check_decay=true,decayable=true,variant=dark_oak]"
  ],
  [
    161,
    12,
    "minecraft:leaves2[check_decay=true,decayable=false,variant=acacia]"
  ],
  [
    161,
    13,
    "minecraft:leaves2[check_decay=true,decayable=false,variant=dark_oak]"
  ],
  [162, 0, "minecraft:log2[axis=y,variant=acacia]"],
  [162, 1, "minecraft:log2[axis=y,variant=dark_oak]"],
  [162, 4, "minecraft:log2[axis=x,variant=acacia]"],
  [162, 5, "minecraft:log2[axis=x,variant=dark_oak]"],
  [162, 8, "minecraft:log2[axis=z,variant=acacia]"],
  [162, 9, "minecraft:log2[axis=z,variant=dark_oak]"],
  [162, 12, "minecraft:log2[axis=none,variant=acacia]"],
  [162, 13, "minecraft:log2[axis=none,variant=dark_oak]"],
  [163, 0, "minecraft:acacia_stairs[facing=east,half=bottom,shape=straight]"],
  [163, 1, "minecraft:acacia_stairs[facing=west,half=bottom,shape=straight]"],
  [163, 2, "minecraft:acacia_stairs[facing=south,half=bottom,shape=straight]"],
  [163, 3, "minecraft:acacia_stairs[facing=north,half=bottom,shape=straight]"],
  [163, 4, "minecraft:acacia_stairs[facing=east,half=top,shape=straight]"],
  [163, 5, "minecraft:acacia_stairs[facing=west,half=top,shape=straight]"],
  [163, 6, "minecraft:acacia_stairs[facing=south,half=top,shape=straight]"],
  [163, 7, "minecraft:acacia_stairs[facing=north,half=top,shape=straight]"],
  [164, 0, "minecraft:dark_oak_stairs[facing=east,half=bottom,shape=straight]"],
  [164, 1, "minecraft:dark_oak_stairs[facing=west,half=bottom,shape=straight]"],
  [
    164,
    2,
    "minecraft:dark_oak_stairs[facing=south,half=bottom,shape=straight]"
  ],
  [
    164,
    3,
    "minecraft:dark_oak_stairs[facing=north,half=bottom,shape=straight]"
  ],
  [164, 4, "minecraft:dark_oak_stairs[facing=east,half=top,shape=straight]"],
  [164, 5, "minecraft:dark_oak_stairs[facing=west,half=top,shape=straight]"],
  [164, 6, "minecraft:dark_oak_stairs[facing=south,half=top,shape=straight]"],
  [164, 7, "minecraft:dark_oak_stairs[facing=north,half=top,shape=straight]"],
  [165, 0, "minecraft:slime"],
  [166, 0, "minecraft:barrier"],
  [167, 0, "minecraft:iron_trapdoor[facing=north,half=bottom,open=false]"],
  [167, 1, "minecraft:iron_trapdoor[facing=south,half=bottom,open=false]"],
  [167, 2, "minecraft:iron_trapdoor[facing=west,half=bottom,open=false]"],
  [167, 3, "minecraft:iron_trapdoor[facing=east,half=bottom,open=false]"],
  [167, 4, "minecraft:iron_trapdoor[facing=north,half=bottom,open=true]"],
  [167, 5, "minecraft:iron_trapdoor[facing=south,half=bottom,open=true]"],
  [167, 6, "minecraft:iron_trapdoor[facing=west,half=bottom,open=true]"],
  [167, 7, "minecraft:iron_trapdoor[facing=east,half=bottom,open=true]"],
  [167, 8, "minecraft:iron_trapdoor[facing=north,half=top,open=false]"],
  [167, 9, "minecraft:iron_trapdoor[facing=south,half=top,open=false]"],
  [167, 10, "minecraft:iron_trapdoor[facing=west,half=top,open=false]"],
  [167, 11, "minecraft:iron_trapdoor[facing=east,half=top,open=false]"],
  [167, 12, "minecraft:iron_trapdoor[facing=north,half=top,open=true]"],
  [167, 13, "minecraft:iron_trapdoor[facing=south,half=top,open=true]"],
  [167, 14, "minecraft:iron_trapdoor[facing=west,half=top,open=true]"],
  [167, 15, "minecraft:iron_trapdoor[facing=east,half=top,open=true]"],
  [168, 0, "minecraft:prismarine[variant=prismarine]"],
  [168, 1, "minecraft:prismarine[variant=prismarine_bricks]"],
  [168, 2, "minecraft:prismarine[variant=dark_prismarine]"],
  [169, 0, "minecraft:sea_lantern"],
  [170, 0, "minecraft:hay_block[axis=y]"],
  [170, 4, "minecraft:hay_block[axis=x]"],
  [170, 8, "minecraft:hay_block[axis=z]"],
  [171, 0, "minecraft:carpet[color=white]"],
  [171, 1, "minecraft:carpet[color=orange]"],
  [171, 2, "minecraft:carpet[color=magenta]"],
  [171, 3, "minecraft:carpet[color=light_blue]"],
  [171, 4, "minecraft:carpet[color=yellow]"],
  [171, 5, "minecraft:carpet[color=lime]"],
  [171, 6, "minecraft:carpet[color=pink]"],
  [171, 7, "minecraft:carpet[color=gray]"],
  [171, 8, "minecraft:carpet[color=silver]"],
  [171, 9, "minecraft:carpet[color=cyan]"],
  [171, 10, "minecraft:carpet[color=purple]"],
  [171, 11, "minecraft:carpet[color=blue]"],
  [171, 12, "minecraft:carpet[color=brown]"],
  [171, 13, "minecraft:carpet[color=green]"],
  [171, 14, "minecraft:carpet[color=red]"],
  [171, 15, "minecraft:carpet[color=black]"],
  [172, 0, "minecraft:hardened_clay"],
  [173, 0, "minecraft:coal_block"],
  [174, 0, "minecraft:packed_ice"],
  [175, 0, "minecraft:double_plant[facing=north,half=lower,variant=sunflower]"],
  [175, 1, "minecraft:double_plant[facing=north,half=lower,variant=syringa]"],
  [
    175,
    2,
    "minecraft:double_plant[facing=north,half=lower,variant=double_grass]"
  ],
  [
    175,
    3,
    "minecraft:double_plant[facing=north,half=lower,variant=double_fern]"
  ],
  [
    175,
    4,
    "minecraft:double_plant[facing=north,half=lower,variant=double_rose]"
  ],
  [175, 5, "minecraft:double_plant[facing=north,half=lower,variant=paeonia]"],
  [175, 8, "minecraft:double_plant[facing=north,half=upper,variant=sunflower]"],
  [176, 0, "minecraft:standing_banner[rotation=0]"],
  [176, 1, "minecraft:standing_banner[rotation=1]"],
  [176, 2, "minecraft:standing_banner[rotation=2]"],
  [176, 3, "minecraft:standing_banner[rotation=3]"],
  [176, 4, "minecraft:standing_banner[rotation=4]"],
  [176, 5, "minecraft:standing_banner[rotation=5]"],
  [176, 6, "minecraft:standing_banner[rotation=6]"],
  [176, 7, "minecraft:standing_banner[rotation=7]"],
  [176, 8, "minecraft:standing_banner[rotation=8]"],
  [176, 9, "minecraft:standing_banner[rotation=9]"],
  [176, 10, "minecraft:standing_banner[rotation=10]"],
  [176, 11, "minecraft:standing_banner[rotation=11]"],
  [176, 12, "minecraft:standing_banner[rotation=12]"],
  [176, 13, "minecraft:standing_banner[rotation=13]"],
  [176, 14, "minecraft:standing_banner[rotation=14]"],
  [176, 15, "minecraft:standing_banner[rotation=15]"],
  [177, 0, "minecraft:wall_banner[facing=north]"],
  [177, 3, "minecraft:wall_banner[facing=south]"],
  [177, 4, "minecraft:wall_banner[facing=west]"],
  [177, 5, "minecraft:wall_banner[facing=east]"],
  [178, 0, "minecraft:daylight_detector_inverted[power=0]"],
  [178, 1, "minecraft:daylight_detector_inverted[power=1]"],
  [178, 2, "minecraft:daylight_detector_inverted[power=2]"],
  [178, 3, "minecraft:daylight_detector_inverted[power=3]"],
  [178, 4, "minecraft:daylight_detector_inverted[power=4]"],
  [178, 5, "minecraft:daylight_detector_inverted[power=5]"],
  [178, 6, "minecraft:daylight_detector_inverted[power=6]"],
  [178, 7, "minecraft:daylight_detector_inverted[power=7]"],
  [178, 8, "minecraft:daylight_detector_inverted[power=8]"],
  [178, 9, "minecraft:daylight_detector_inverted[power=9]"],
  [178, 10, "minecraft:daylight_detector_inverted[power=10]"],
  [178, 11, "minecraft:daylight_detector_inverted[power=11]"],
  [178, 12, "minecraft:daylight_detector_inverted[power=12]"],
  [178, 13, "minecraft:daylight_detector_inverted[power=13]"],
  [178, 14, "minecraft:daylight_detector_inverted[power=14]"],
  [178, 15, "minecraft:daylight_detector_inverted[power=15]"],
  [179, 0, "minecraft:red_sandstone[type=red_sandstone]"],
  [179, 1, "minecraft:red_sandstone[type=chiseled_red_sandstone]"],
  [179, 2, "minecraft:red_sandstone[type=smooth_red_sandstone]"],
  [
    180,
    0,
    "minecraft:red_sandstone_stairs[facing=east,half=bottom,shape=straight]"
  ],
  [
    180,
    1,
    "minecraft:red_sandstone_stairs[facing=west,half=bottom,shape=straight]"
  ],
  [
    180,
    2,
    "minecraft:red_sandstone_stairs[facing=south,half=bottom,shape=straight]"
  ],
  [
    180,
    3,
    "minecraft:red_sandstone_stairs[facing=north,half=bottom,shape=straight]"
  ],
  [
    180,
    4,
    "minecraft:red_sandstone_stairs[facing=east,half=top,shape=straight]"
  ],
  [
    180,
    5,
    "minecraft:red_sandstone_stairs[facing=west,half=top,shape=straight]"
  ],
  [
    180,
    6,
    "minecraft:red_sandstone_stairs[facing=south,half=top,shape=straight]"
  ],
  [
    180,
    7,
    "minecraft:red_sandstone_stairs[facing=north,half=top,shape=straight]"
  ],
  [
    181,
    0,
    "minecraft:double_stone_slab2[seamless=false,variant=red_sandstone]"
  ],
  [181, 8, "minecraft:double_stone_slab2[seamless=true,variant=red_sandstone]"],
  [182, 0, "minecraft:stone_slab2[half=bottom,variant=red_sandstone]"],
  [182, 8, "minecraft:stone_slab2[half=top,variant=red_sandstone]"],
  [
    183,
    0,
    "minecraft:spruce_fence_gate[facing=south,in_wall=false,open=false,powered=false]"
  ],
  [
    183,
    1,
    "minecraft:spruce_fence_gate[facing=west,in_wall=false,open=false,powered=false]"
  ],
  [
    183,
    2,
    "minecraft:spruce_fence_gate[facing=north,in_wall=false,open=false,powered=false]"
  ],
  [
    183,
    3,
    "minecraft:spruce_fence_gate[facing=east,in_wall=false,open=false,powered=false]"
  ],
  [
    183,
    4,
    "minecraft:spruce_fence_gate[facing=south,in_wall=false,open=true,powered=false]"
  ],
  [
    183,
    5,
    "minecraft:spruce_fence_gate[facing=west,in_wall=false,open=true,powered=false]"
  ],
  [
    183,
    6,
    "minecraft:spruce_fence_gate[facing=north,in_wall=false,open=true,powered=false]"
  ],
  [
    183,
    7,
    "minecraft:spruce_fence_gate[facing=east,in_wall=false,open=true,powered=false]"
  ],
  [
    183,
    8,
    "minecraft:spruce_fence_gate[facing=south,in_wall=false,open=false,powered=true]"
  ],
  [
    183,
    9,
    "minecraft:spruce_fence_gate[facing=west,in_wall=false,open=false,powered=true]"
  ],
  [
    183,
    10,
    "minecraft:spruce_fence_gate[facing=north,in_wall=false,open=false,powered=true]"
  ],
  [
    183,
    11,
    "minecraft:spruce_fence_gate[facing=east,in_wall=false,open=false,powered=true]"
  ],
  [
    183,
    12,
    "minecraft:spruce_fence_gate[facing=south,in_wall=false,open=true,powered=true]"
  ],
  [
    183,
    13,
    "minecraft:spruce_fence_gate[facing=west,in_wall=false,open=true,powered=true]"
  ],
  [
    183,
    14,
    "minecraft:spruce_fence_gate[facing=north,in_wall=false,open=true,powered=true]"
  ],
  [
    183,
    15,
    "minecraft:spruce_fence_gate[facing=east,in_wall=false,open=true,powered=true]"
  ],
  [
    184,
    0,
    "minecraft:birch_fence_gate[facing=south,in_wall=false,open=false,powered=false]"
  ],
  [
    184,
    1,
    "minecraft:birch_fence_gate[facing=west,in_wall=false,open=false,powered=false]"
  ],
  [
    184,
    2,
    "minecraft:birch_fence_gate[facing=north,in_wall=false,open=false,powered=false]"
  ],
  [
    184,
    3,
    "minecraft:birch_fence_gate[facing=east,in_wall=false,open=false,powered=false]"
  ],
  [
    184,
    4,
    "minecraft:birch_fence_gate[facing=south,in_wall=false,open=true,powered=false]"
  ],
  [
    184,
    5,
    "minecraft:birch_fence_gate[facing=west,in_wall=false,open=true,powered=false]"
  ],
  [
    184,
    6,
    "minecraft:birch_fence_gate[facing=north,in_wall=false,open=true,powered=false]"
  ],
  [
    184,
    7,
    "minecraft:birch_fence_gate[facing=east,in_wall=false,open=true,powered=false]"
  ],
  [
    184,
    8,
    "minecraft:birch_fence_gate[facing=south,in_wall=false,open=false,powered=true]"
  ],
  [
    184,
    9,
    "minecraft:birch_fence_gate[facing=west,in_wall=false,open=false,powered=true]"
  ],
  [
    184,
    10,
    "minecraft:birch_fence_gate[facing=north,in_wall=false,open=false,powered=true]"
  ],
  [
    184,
    11,
    "minecraft:birch_fence_gate[facing=east,in_wall=false,open=false,powered=true]"
  ],
  [
    184,
    12,
    "minecraft:birch_fence_gate[facing=south,in_wall=false,open=true,powered=true]"
  ],
  [
    184,
    13,
    "minecraft:birch_fence_gate[facing=west,in_wall=false,open=true,powered=true]"
  ],
  [
    184,
    14,
    "minecraft:birch_fence_gate[facing=north,in_wall=false,open=true,powered=true]"
  ],
  [
    184,
    15,
    "minecraft:birch_fence_gate[facing=east,in_wall=false,open=true,powered=true]"
  ],
  [
    185,
    0,
    "minecraft:jungle_fence_gate[facing=south,in_wall=false,open=false,powered=false]"
  ],
  [
    185,
    1,
    "minecraft:jungle_fence_gate[facing=west,in_wall=false,open=false,powered=false]"
  ],
  [
    185,
    2,
    "minecraft:jungle_fence_gate[facing=north,in_wall=false,open=false,powered=false]"
  ],
  [
    185,
    3,
    "minecraft:jungle_fence_gate[facing=east,in_wall=false,open=false,powered=false]"
  ],
  [
    185,
    4,
    "minecraft:jungle_fence_gate[facing=south,in_wall=false,open=true,powered=false]"
  ],
  [
    185,
    5,
    "minecraft:jungle_fence_gate[facing=west,in_wall=false,open=true,powered=false]"
  ],
  [
    185,
    6,
    "minecraft:jungle_fence_gate[facing=north,in_wall=false,open=true,powered=false]"
  ],
  [
    185,
    7,
    "minecraft:jungle_fence_gate[facing=east,in_wall=false,open=true,powered=false]"
  ],
  [
    185,
    8,
    "minecraft:jungle_fence_gate[facing=south,in_wall=false,open=false,powered=true]"
  ],
  [
    185,
    9,
    "minecraft:jungle_fence_gate[facing=west,in_wall=false,open=false,powered=true]"
  ],
  [
    185,
    10,
    "minecraft:jungle_fence_gate[facing=north,in_wall=false,open=false,powered=true]"
  ],
  [
    185,
    11,
    "minecraft:jungle_fence_gate[facing=east,in_wall=false,open=false,powered=true]"
  ],
  [
    185,
    12,
    "minecraft:jungle_fence_gate[facing=south,in_wall=false,open=true,powered=true]"
  ],
  [
    185,
    13,
    "minecraft:jungle_fence_gate[facing=west,in_wall=false,open=true,powered=true]"
  ],
  [
    185,
    14,
    "minecraft:jungle_fence_gate[facing=north,in_wall=false,open=true,powered=true]"
  ],
  [
    185,
    15,
    "minecraft:jungle_fence_gate[facing=east,in_wall=false,open=true,powered=true]"
  ],
  [
    186,
    0,
    "minecraft:dark_oak_fence_gate[facing=south,in_wall=false,open=false,powered=false]"
  ],
  [
    186,
    1,
    "minecraft:dark_oak_fence_gate[facing=west,in_wall=false,open=false,powered=false]"
  ],
  [
    186,
    2,
    "minecraft:dark_oak_fence_gate[facing=north,in_wall=false,open=false,powered=false]"
  ],
  [
    186,
    3,
    "minecraft:dark_oak_fence_gate[facing=east,in_wall=false,open=false,powered=false]"
  ],
  [
    186,
    4,
    "minecraft:dark_oak_fence_gate[facing=south,in_wall=false,open=true,powered=false]"
  ],
  [
    186,
    5,
    "minecraft:dark_oak_fence_gate[facing=west,in_wall=false,open=true,powered=false]"
  ],
  [
    186,
    6,
    "minecraft:dark_oak_fence_gate[facing=north,in_wall=false,open=true,powered=false]"
  ],
  [
    186,
    7,
    "minecraft:dark_oak_fence_gate[facing=east,in_wall=false,open=true,powered=false]"
  ],
  [
    186,
    8,
    "minecraft:dark_oak_fence_gate[facing=south,in_wall=false,open=false,powered=true]"
  ],
  [
    186,
    9,
    "minecraft:dark_oak_fence_gate[facing=west,in_wall=false,open=false,powered=true]"
  ],
  [
    186,
    10,
    "minecraft:dark_oak_fence_gate[facing=north,in_wall=false,open=false,powered=true]"
  ],
  [
    186,
    11,
    "minecraft:dark_oak_fence_gate[facing=east,in_wall=false,open=false,powered=true]"
  ],
  [
    186,
    12,
    "minecraft:dark_oak_fence_gate[facing=south,in_wall=false,open=true,powered=true]"
  ],
  [
    186,
    13,
    "minecraft:dark_oak_fence_gate[facing=west,in_wall=false,open=true,powered=true]"
  ],
  [
    186,
    14,
    "minecraft:dark_oak_fence_gate[facing=north,in_wall=false,open=true,powered=true]"
  ],
  [
    186,
    15,
    "minecraft:dark_oak_fence_gate[facing=east,in_wall=false,open=true,powered=true]"
  ],
  [
    187,
    0,
    "minecraft:acacia_fence_gate[facing=south,in_wall=false,open=false,powered=false]"
  ],
  [
    187,
    1,
    "minecraft:acacia_fence_gate[facing=west,in_wall=false,open=false,powered=false]"
  ],
  [
    187,
    2,
    "minecraft:acacia_fence_gate[facing=north,in_wall=false,open=false,powered=false]"
  ],
  [
    187,
    3,
    "minecraft:acacia_fence_gate[facing=east,in_wall=false,open=false,powered=false]"
  ],
  [
    187,
    4,
    "minecraft:acacia_fence_gate[facing=south,in_wall=false,open=true,powered=false]"
  ],
  [
    187,
    5,
    "minecraft:acacia_fence_gate[facing=west,in_wall=false,open=true,powered=false]"
  ],
  [
    187,
    6,
    "minecraft:acacia_fence_gate[facing=north,in_wall=false,open=true,powered=false]"
  ],
  [
    187,
    7,
    "minecraft:acacia_fence_gate[facing=east,in_wall=false,open=true,powered=false]"
  ],
  [
    187,
    8,
    "minecraft:acacia_fence_gate[facing=south,in_wall=false,open=false,powered=true]"
  ],
  [
    187,
    9,
    "minecraft:acacia_fence_gate[facing=west,in_wall=false,open=false,powered=true]"
  ],
  [
    187,
    10,
    "minecraft:acacia_fence_gate[facing=north,in_wall=false,open=false,powered=true]"
  ],
  [
    187,
    11,
    "minecraft:acacia_fence_gate[facing=east,in_wall=false,open=false,powered=true]"
  ],
  [
    187,
    12,
    "minecraft:acacia_fence_gate[facing=south,in_wall=false,open=true,powered=true]"
  ],
  [
    187,
    13,
    "minecraft:acacia_fence_gate[facing=west,in_wall=false,open=true,powered=true]"
  ],
  [
    187,
    14,
    "minecraft:acacia_fence_gate[facing=north,in_wall=false,open=true,powered=true]"
  ],
  [
    187,
    15,
    "minecraft:acacia_fence_gate[facing=east,in_wall=false,open=true,powered=true]"
  ],
  [
    188,
    0,
    "minecraft:spruce_fence[east=false,north=false,south=false,west=false]"
  ],
  [
    189,
    0,
    "minecraft:birch_fence[east=false,north=false,south=false,west=false]"
  ],
  [
    190,
    0,
    "minecraft:jungle_fence[east=false,north=false,south=false,west=false]"
  ],
  [
    191,
    0,
    "minecraft:dark_oak_fence[east=false,north=false,south=false,west=false]"
  ],
  [
    192,
    0,
    "minecraft:acacia_fence[east=false,north=false,south=false,west=false]"
  ],
  [
    193,
    0,
    "minecraft:spruce_door[facing=east,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    193,
    1,
    "minecraft:spruce_door[facing=south,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    193,
    2,
    "minecraft:spruce_door[facing=west,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    193,
    3,
    "minecraft:spruce_door[facing=north,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    193,
    4,
    "minecraft:spruce_door[facing=east,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    193,
    5,
    "minecraft:spruce_door[facing=south,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    193,
    6,
    "minecraft:spruce_door[facing=west,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    193,
    7,
    "minecraft:spruce_door[facing=north,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    193,
    8,
    "minecraft:spruce_door[facing=north,half=upper,hinge=left,open=false,powered=false]"
  ],
  [
    193,
    9,
    "minecraft:spruce_door[facing=north,half=upper,hinge=right,open=false,powered=false]"
  ],
  [
    193,
    10,
    "minecraft:spruce_door[facing=north,half=upper,hinge=left,open=false,powered=true]"
  ],
  [
    193,
    11,
    "minecraft:spruce_door[facing=north,half=upper,hinge=right,open=false,powered=true]"
  ],
  [
    194,
    0,
    "minecraft:birch_door[facing=east,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    194,
    1,
    "minecraft:birch_door[facing=south,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    194,
    2,
    "minecraft:birch_door[facing=west,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    194,
    3,
    "minecraft:birch_door[facing=north,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    194,
    4,
    "minecraft:birch_door[facing=east,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    194,
    5,
    "minecraft:birch_door[facing=south,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    194,
    6,
    "minecraft:birch_door[facing=west,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    194,
    7,
    "minecraft:birch_door[facing=north,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    194,
    8,
    "minecraft:birch_door[facing=north,half=upper,hinge=left,open=false,powered=false]"
  ],
  [
    194,
    9,
    "minecraft:birch_door[facing=north,half=upper,hinge=right,open=false,powered=false]"
  ],
  [
    194,
    10,
    "minecraft:birch_door[facing=north,half=upper,hinge=left,open=false,powered=true]"
  ],
  [
    194,
    11,
    "minecraft:birch_door[facing=north,half=upper,hinge=right,open=false,powered=true]"
  ],
  [
    195,
    0,
    "minecraft:jungle_door[facing=east,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    195,
    1,
    "minecraft:jungle_door[facing=south,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    195,
    2,
    "minecraft:jungle_door[facing=west,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    195,
    3,
    "minecraft:jungle_door[facing=north,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    195,
    4,
    "minecraft:jungle_door[facing=east,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    195,
    5,
    "minecraft:jungle_door[facing=south,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    195,
    6,
    "minecraft:jungle_door[facing=west,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    195,
    7,
    "minecraft:jungle_door[facing=north,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    195,
    8,
    "minecraft:jungle_door[facing=north,half=upper,hinge=left,open=false,powered=false]"
  ],
  [
    195,
    9,
    "minecraft:jungle_door[facing=north,half=upper,hinge=right,open=false,powered=false]"
  ],
  [
    195,
    10,
    "minecraft:jungle_door[facing=north,half=upper,hinge=left,open=false,powered=true]"
  ],
  [
    195,
    11,
    "minecraft:jungle_door[facing=north,half=upper,hinge=right,open=false,powered=true]"
  ],
  [
    196,
    0,
    "minecraft:acacia_door[facing=east,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    196,
    1,
    "minecraft:acacia_door[facing=south,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    196,
    2,
    "minecraft:acacia_door[facing=west,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    196,
    3,
    "minecraft:acacia_door[facing=north,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    196,
    4,
    "minecraft:acacia_door[facing=east,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    196,
    5,
    "minecraft:acacia_door[facing=south,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    196,
    6,
    "minecraft:acacia_door[facing=west,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    196,
    7,
    "minecraft:acacia_door[facing=north,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    196,
    8,
    "minecraft:acacia_door[facing=north,half=upper,hinge=left,open=false,powered=false]"
  ],
  [
    196,
    9,
    "minecraft:acacia_door[facing=north,half=upper,hinge=right,open=false,powered=false]"
  ],
  [
    196,
    10,
    "minecraft:acacia_door[facing=north,half=upper,hinge=left,open=false,powered=true]"
  ],
  [
    196,
    11,
    "minecraft:acacia_door[facing=north,half=upper,hinge=right,open=false,powered=true]"
  ],
  [
    197,
    0,
    "minecraft:dark_oak_door[facing=east,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    197,
    1,
    "minecraft:dark_oak_door[facing=south,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    197,
    2,
    "minecraft:dark_oak_door[facing=west,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    197,
    3,
    "minecraft:dark_oak_door[facing=north,half=lower,hinge=left,open=false,powered=false]"
  ],
  [
    197,
    4,
    "minecraft:dark_oak_door[facing=east,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    197,
    5,
    "minecraft:dark_oak_door[facing=south,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    197,
    6,
    "minecraft:dark_oak_door[facing=west,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    197,
    7,
    "minecraft:dark_oak_door[facing=north,half=lower,hinge=left,open=true,powered=false]"
  ],
  [
    197,
    8,
    "minecraft:dark_oak_door[facing=north,half=upper,hinge=left,open=false,powered=false]"
  ],
  [
    197,
    9,
    "minecraft:dark_oak_door[facing=north,half=upper,hinge=right,open=false,powered=false]"
  ],
  [
    197,
    10,
    "minecraft:dark_oak_door[facing=north,half=upper,hinge=left,open=false,powered=true]"
  ],
  [
    197,
    11,
    "minecraft:dark_oak_door[facing=north,half=upper,hinge=right,open=false,powered=true]"
  ],
  [198, 0, "minecraft:end_rod[facing=down]"],
  [198, 1, "minecraft:end_rod[facing=up]"],
  [198, 2, "minecraft:end_rod[facing=north]"],
  [198, 3, "minecraft:end_rod[facing=south]"],
  [198, 4, "minecraft:end_rod[facing=west]"],
  [198, 5, "minecraft:end_rod[facing=east]"],
  [
    199,
    0,
    "minecraft:chorus_plant[down=false,east=false,north=false,south=false,up=false,west=false]"
  ],
  [200, 0, "minecraft:chorus_flower[age=0]"],
  [200, 1, "minecraft:chorus_flower[age=1]"],
  [200, 2, "minecraft:chorus_flower[age=2]"],
  [200, 3, "minecraft:chorus_flower[age=3]"],
  [200, 4, "minecraft:chorus_flower[age=4]"],
  [200, 5, "minecraft:chorus_flower[age=5]"],
  [201, 0, "minecraft:purpur_block"],
  [202, 0, "minecraft:purpur_pillar[axis=y]"],
  [202, 4, "minecraft:purpur_pillar[axis=x]"],
  [202, 8, "minecraft:purpur_pillar[axis=z]"],
  [203, 0, "minecraft:purpur_stairs[facing=east,half=bottom,shape=straight]"],
  [203, 1, "minecraft:purpur_stairs[facing=west,half=bottom,shape=straight]"],
  [203, 2, "minecraft:purpur_stairs[facing=south,half=bottom,shape=straight]"],
  [203, 3, "minecraft:purpur_stairs[facing=north,half=bottom,shape=straight]"],
  [203, 4, "minecraft:purpur_stairs[facing=east,half=top,shape=straight]"],
  [203, 5, "minecraft:purpur_stairs[facing=west,half=top,shape=straight]"],
  [203, 6, "minecraft:purpur_stairs[facing=south,half=top,shape=straight]"],
  [203, 7, "minecraft:purpur_stairs[facing=north,half=top,shape=straight]"],
  [204, 0, "minecraft:purpur_double_slab[variant=default]"],
  [205, 0, "minecraft:purpur_slab[half=bottom,variant=default]"],
  [205, 8, "minecraft:purpur_slab[half=top,variant=default]"],
  [206, 0, "minecraft:end_bricks"],
  [207, 0, "minecraft:beetroots[age=0]"],
  [207, 1, "minecraft:beetroots[age=1]"],
  [207, 2, "minecraft:beetroots[age=2]"],
  [207, 3, "minecraft:beetroots[age=3]"],
  [208, 0, "minecraft:grass_path"],
  [209, 0, "minecraft:end_gateway"],
  [210, 0, "minecraft:repeating_command_block[conditional=false,facing=down]"],
  [210, 1, "minecraft:repeating_command_block[conditional=false,facing=up]"],
  [210, 2, "minecraft:repeating_command_block[conditional=false,facing=north]"],
  [210, 3, "minecraft:repeating_command_block[conditional=false,facing=south]"],
  [210, 4, "minecraft:repeating_command_block[conditional=false,facing=west]"],
  [210, 5, "minecraft:repeating_command_block[conditional=false,facing=east]"],
  [210, 8, "minecraft:repeating_command_block[conditional=true,facing=down]"],
  [210, 9, "minecraft:repeating_command_block[conditional=true,facing=up]"],
  [210, 10, "minecraft:repeating_command_block[conditional=true,facing=north]"],
  [210, 11, "minecraft:repeating_command_block[conditional=true,facing=south]"],
  [210, 12, "minecraft:repeating_command_block[conditional=true,facing=west]"],
  [210, 13, "minecraft:repeating_command_block[conditional=true,facing=east]"],
  [211, 0, "minecraft:chain_command_block[conditional=false,facing=down]"],
  [211, 1, "minecraft:chain_command_block[conditional=false,facing=up]"],
  [211, 2, "minecraft:chain_command_block[conditional=false,facing=north]"],
  [211, 3, "minecraft:chain_command_block[conditional=false,facing=south]"],
  [211, 4, "minecraft:chain_command_block[conditional=false,facing=west]"],
  [211, 5, "minecraft:chain_command_block[conditional=false,facing=east]"],
  [211, 8, "minecraft:chain_command_block[conditional=true,facing=down]"],
  [211, 9, "minecraft:chain_command_block[conditional=true,facing=up]"],
  [211, 10, "minecraft:chain_command_block[conditional=true,facing=north]"],
  [211, 11, "minecraft:chain_command_block[conditional=true,facing=south]"],
  [211, 12, "minecraft:chain_command_block[conditional=true,facing=west]"],
  [211, 13, "minecraft:chain_command_block[conditional=true,facing=east]"],
  [212, 0, "minecraft:frosted_ice[age=0]"],
  [212, 1, "minecraft:frosted_ice[age=1]"],
  [212, 2, "minecraft:frosted_ice[age=2]"],
  [212, 3, "minecraft:frosted_ice[age=3]"],
  [213, 0, "minecraft:magma"],
  [214, 0, "minecraft:nether_wart_block"],
  [215, 0, "minecraft:red_nether_brick"],
  [216, 0, "minecraft:bone_block[axis=y]"],
  [216, 4, "minecraft:bone_block[axis=x]"],
  [216, 8, "minecraft:bone_block[axis=z]"],
  [217, 0, "minecraft:structure_void"],
  [218, 0, "minecraft:observer[facing=down,powered=false]"],
  [218, 1, "minecraft:observer[facing=up,powered=false]"],
  [218, 2, "minecraft:observer[facing=north,powered=false]"],
  [218, 3, "minecraft:observer[facing=south,powered=false]"],
  [218, 4, "minecraft:observer[facing=west,powered=false]"],
  [218, 5, "minecraft:observer[facing=east,powered=false]"],
  [219, 0, "minecraft:white_shulker_box[facing=down]"],
  [219, 1, "minecraft:white_shulker_box[facing=up]"],
  [219, 2, "minecraft:white_shulker_box[facing=north]"],
  [219, 3, "minecraft:white_shulker_box[facing=south]"],
  [219, 4, "minecraft:white_shulker_box[facing=west]"],
  [219, 5, "minecraft:white_shulker_box[facing=east]"],
  [220, 0, "minecraft:orange_shulker_box[facing=down]"],
  [220, 1, "minecraft:orange_shulker_box[facing=up]"],
  [220, 2, "minecraft:orange_shulker_box[facing=north]"],
  [220, 3, "minecraft:orange_shulker_box[facing=south]"],
  [220, 4, "minecraft:orange_shulker_box[facing=west]"],
  [220, 5, "minecraft:orange_shulker_box[facing=east]"],
  [221, 0, "minecraft:magenta_shulker_box[facing=down]"],
  [221, 1, "minecraft:magenta_shulker_box[facing=up]"],
  [221, 2, "minecraft:magenta_shulker_box[facing=north]"],
  [221, 3, "minecraft:magenta_shulker_box[facing=south]"],
  [221, 4, "minecraft:magenta_shulker_box[facing=west]"],
  [221, 5, "minecraft:magenta_shulker_box[facing=east]"],
  [222, 0, "minecraft:light_blue_shulker_box[facing=down]"],
  [222, 1, "minecraft:light_blue_shulker_box[facing=up]"],
  [222, 2, "minecraft:light_blue_shulker_box[facing=north]"],
  [222, 3, "minecraft:light_blue_shulker_box[facing=south]"],
  [222, 4, "minecraft:light_blue_shulker_box[facing=west]"],
  [222, 5, "minecraft:light_blue_shulker_box[facing=east]"],
  [223, 0, "minecraft:yellow_shulker_box[facing=down]"],
  [223, 1, "minecraft:yellow_shulker_box[facing=up]"],
  [223, 2, "minecraft:yellow_shulker_box[facing=north]"],
  [223, 3, "minecraft:yellow_shulker_box[facing=south]"],
  [223, 4, "minecraft:yellow_shulker_box[facing=west]"],
  [223, 5, "minecraft:yellow_shulker_box[facing=east]"],
  [224, 0, "minecraft:lime_shulker_box[facing=down]"],
  [224, 1, "minecraft:lime_shulker_box[facing=up]"],
  [224, 2, "minecraft:lime_shulker_box[facing=north]"],
  [224, 3, "minecraft:lime_shulker_box[facing=south]"],
  [224, 4, "minecraft:lime_shulker_box[facing=west]"],
  [224, 5, "minecraft:lime_shulker_box[facing=east]"],
  [225, 0, "minecraft:pink_shulker_box[facing=down]"],
  [225, 1, "minecraft:pink_shulker_box[facing=up]"],
  [225, 2, "minecraft:pink_shulker_box[facing=north]"],
  [225, 3, "minecraft:pink_shulker_box[facing=south]"],
  [225, 4, "minecraft:pink_shulker_box[facing=west]"],
  [225, 5, "minecraft:pink_shulker_box[facing=east]"],
  [226, 0, "minecraft:gray_shulker_box[facing=down]"],
  [226, 1, "minecraft:gray_shulker_box[facing=up]"],
  [226, 2, "minecraft:gray_shulker_box[facing=north]"],
  [226, 3, "minecraft:gray_shulker_box[facing=south]"],
  [226, 4, "minecraft:gray_shulker_box[facing=west]"],
  [226, 5, "minecraft:gray_shulker_box[facing=east]"],
  [228, 0, "minecraft:cyan_shulker_box[facing=down]"],
  [228, 1, "minecraft:cyan_shulker_box[facing=up]"],
  [228, 2, "minecraft:cyan_shulker_box[facing=north]"],
  [228, 3, "minecraft:cyan_shulker_box[facing=south]"],
  [228, 4, "minecraft:cyan_shulker_box[facing=west]"],
  [228, 5, "minecraft:cyan_shulker_box[facing=east]"],
  [229, 0, "minecraft:purple_shulker_box[facing=down]"],
  [229, 1, "minecraft:purple_shulker_box[facing=up]"],
  [229, 2, "minecraft:purple_shulker_box[facing=north]"],
  [229, 3, "minecraft:purple_shulker_box[facing=south]"],
  [229, 4, "minecraft:purple_shulker_box[facing=west]"],
  [229, 5, "minecraft:purple_shulker_box[facing=east]"],
  [230, 0, "minecraft:blue_shulker_box[facing=down]"],
  [230, 1, "minecraft:blue_shulker_box[facing=up]"],
  [230, 2, "minecraft:blue_shulker_box[facing=north]"],
  [230, 3, "minecraft:blue_shulker_box[facing=south]"],
  [230, 4, "minecraft:blue_shulker_box[facing=west]"],
  [230, 5, "minecraft:blue_shulker_box[facing=east]"],
  [231, 0, "minecraft:brown_shulker_box[facing=down]"],
  [231, 1, "minecraft:brown_shulker_box[facing=up]"],
  [231, 2, "minecraft:brown_shulker_box[facing=north]"],
  [231, 3, "minecraft:brown_shulker_box[facing=south]"],
  [231, 4, "minecraft:brown_shulker_box[facing=west]"],
  [231, 5, "minecraft:brown_shulker_box[facing=east]"],
  [232, 0, "minecraft:green_shulker_box[facing=down]"],
  [232, 1, "minecraft:green_shulker_box[facing=up]"],
  [232, 2, "minecraft:green_shulker_box[facing=north]"],
  [232, 3, "minecraft:green_shulker_box[facing=south]"],
  [232, 4, "minecraft:green_shulker_box[facing=west]"],
  [232, 5, "minecraft:green_shulker_box[facing=east]"],
  [233, 0, "minecraft:red_shulker_box[facing=down]"],
  [233, 1, "minecraft:red_shulker_box[facing=up]"],
  [233, 2, "minecraft:red_shulker_box[facing=north]"],
  [233, 3, "minecraft:red_shulker_box[facing=south]"],
  [233, 4, "minecraft:red_shulker_box[facing=west]"],
  [233, 5, "minecraft:red_shulker_box[facing=east]"],
  [234, 0, "minecraft:black_shulker_box[facing=down]"],
  [234, 1, "minecraft:black_shulker_box[facing=up]"],
  [234, 2, "minecraft:black_shulker_box[facing=north]"],
  [234, 3, "minecraft:black_shulker_box[facing=south]"],
  [234, 4, "minecraft:black_shulker_box[facing=west]"],
  [234, 5, "minecraft:black_shulker_box[facing=east]"],
  [235, 0, "minecraft:white_glazed_terracotta[facing=south]"],
  [235, 1, "minecraft:white_glazed_terracotta[facing=west]"],
  [235, 2, "minecraft:white_glazed_terracotta[facing=north]"],
  [235, 3, "minecraft:white_glazed_terracotta[facing=east]"],
  [236, 0, "minecraft:orange_glazed_terracotta[facing=south]"],
  [236, 1, "minecraft:orange_glazed_terracotta[facing=west]"],
  [236, 2, "minecraft:orange_glazed_terracotta[facing=north]"],
  [236, 3, "minecraft:orange_glazed_terracotta[facing=east]"],
  [237, 0, "minecraft:magenta_glazed_terracotta[facing=south]"],
  [237, 1, "minecraft:magenta_glazed_terracotta[facing=west]"],
  [237, 2, "minecraft:magenta_glazed_terracotta[facing=north]"],
  [237, 3, "minecraft:magenta_glazed_terracotta[facing=east]"],
  [238, 0, "minecraft:light_blue_glazed_terracotta[facing=south]"],
  [238, 1, "minecraft:light_blue_glazed_terracotta[facing=west]"],
  [238, 2, "minecraft:light_blue_glazed_terracotta[facing=north]"],
  [238, 3, "minecraft:light_blue_glazed_terracotta[facing=east]"],
  [239, 0, "minecraft:yellow_glazed_terracotta[facing=south]"],
  [239, 1, "minecraft:yellow_glazed_terracotta[facing=west]"],
  [239, 2, "minecraft:yellow_glazed_terracotta[facing=north]"],
  [239, 3, "minecraft:yellow_glazed_terracotta[facing=east]"],
  [240, 0, "minecraft:lime_glazed_terracotta[facing=south]"],
  [240, 1, "minecraft:lime_glazed_terracotta[facing=west]"],
  [240, 2, "minecraft:lime_glazed_terracotta[facing=north]"],
  [240, 3, "minecraft:lime_glazed_terracotta[facing=east]"],
  [241, 0, "minecraft:pink_glazed_terracotta[facing=south]"],
  [241, 1, "minecraft:pink_glazed_terracotta[facing=west]"],
  [241, 2, "minecraft:pink_glazed_terracotta[facing=north]"],
  [241, 3, "minecraft:pink_glazed_terracotta[facing=east]"],
  [242, 0, "minecraft:gray_glazed_terracotta[facing=south]"],
  [242, 1, "minecraft:gray_glazed_terracotta[facing=west]"],
  [242, 2, "minecraft:gray_glazed_terracotta[facing=north]"],
  [242, 3, "minecraft:gray_glazed_terracotta[facing=east]"],
  [243, 0, "minecraft:silver_glazed_terracotta[facing=south]"],
  [243, 1, "minecraft:silver_glazed_terracotta[facing=west]"],
  [243, 2, "minecraft:silver_glazed_terracotta[facing=north]"],
  [243, 3, "minecraft:silver_glazed_terracotta[facing=east]"],
  [244, 0, "minecraft:cyan_glazed_terracotta[facing=south]"],
  [244, 1, "minecraft:cyan_glazed_terracotta[facing=west]"],
  [244, 2, "minecraft:cyan_glazed_terracotta[facing=north]"],
  [244, 3, "minecraft:cyan_glazed_terracotta[facing=east]"],
  [245, 0, "minecraft:purple_glazed_terracotta[facing=south]"],
  [245, 1, "minecraft:purple_glazed_terracotta[facing=west]"],
  [245, 2, "minecraft:purple_glazed_terracotta[facing=north]"],
  [245, 3, "minecraft:purple_glazed_terracotta[facing=east]"],
  [246, 0, "minecraft:blue_glazed_terracotta[facing=south]"],
  [246, 1, "minecraft:blue_glazed_terracotta[facing=west]"],
  [246, 2, "minecraft:blue_glazed_terracotta[facing=north]"],
  [246, 3, "minecraft:blue_glazed_terracotta[facing=east]"],
  [247, 0, "minecraft:brown_glazed_terracotta[facing=south]"],
  [247, 1, "minecraft:brown_glazed_terracotta[facing=west]"],
  [247, 2, "minecraft:brown_glazed_terracotta[facing=north]"],
  [247, 3, "minecraft:brown_glazed_terracotta[facing=east]"],
  [248, 0, "minecraft:green_glazed_terracotta[facing=south]"],
  [248, 1, "minecraft:green_glazed_terracotta[facing=west]"],
  [248, 2, "minecraft:green_glazed_terracotta[facing=north]"],
  [248, 3, "minecraft:green_glazed_terracotta[facing=east]"],
  [249, 0, "minecraft:red_glazed_terracotta[facing=south]"],
  [249, 1, "minecraft:red_glazed_terracotta[facing=west]"],
  [249, 2, "minecraft:red_glazed_terracotta[facing=north]"],
  [249, 3, "minecraft:red_glazed_terracotta[facing=east]"],
  [250, 0, "minecraft:black_glazed_terracotta[facing=south]"],
  [250, 1, "minecraft:black_glazed_terracotta[facing=west]"],
  [250, 2, "minecraft:black_glazed_terracotta[facing=north]"],
  [250, 3, "minecraft:black_glazed_terracotta[facing=east]"],
  [251, 0, "minecraft:concrete[color=white]"],
  [251, 1, "minecraft:concrete[color=orange]"],
  [251, 2, "minecraft:concrete[color=magenta]"],
  [251, 3, "minecraft:concrete[color=light_blue]"],
  [251, 4, "minecraft:concrete[color=yellow]"],
  [251, 5, "minecraft:concrete[color=lime]"],
  [251, 6, "minecraft:concrete[color=pink]"],
  [251, 7, "minecraft:concrete[color=gray]"],
  [251, 8, "minecraft:concrete[color=silver]"],
  [251, 9, "minecraft:concrete[color=cyan]"],
  [251, 10, "minecraft:concrete[color=purple]"],
  [251, 11, "minecraft:concrete[color=blue]"],
  [251, 12, "minecraft:concrete[color=brown]"],
  [251, 13, "minecraft:concrete[color=green]"],
  [251, 14, "minecraft:concrete[color=red]"],
  [251, 15, "minecraft:concrete[color=black]"],
  [252, 0, "minecraft:concrete_powder[color=white]"],
  [252, 1, "minecraft:concrete_powder[color=orange]"],
  [252, 2, "minecraft:concrete_powder[color=magenta]"],
  [252, 3, "minecraft:concrete_powder[color=light_blue]"],
  [252, 4, "minecraft:concrete_powder[color=yellow]"],
  [252, 5, "minecraft:concrete_powder[color=lime]"],
  [252, 6, "minecraft:concrete_powder[color=pink]"],
  [252, 7, "minecraft:concrete_powder[color=gray]"],
  [252, 8, "minecraft:concrete_powder[color=silver]"],
  [252, 9, "minecraft:concrete_powder[color=cyan]"],
  [252, 10, "minecraft:concrete_powder[color=purple]"],
  [252, 11, "minecraft:concrete_powder[color=blue]"],
  [252, 12, "minecraft:concrete_powder[color=brown]"],
  [252, 13, "minecraft:concrete_powder[color=green]"],
  [252, 14, "minecraft:concrete_powder[color=red]"],
  [252, 15, "minecraft:concrete_powder[color=black]"],
  [255, 0, "minecraft:structure_block[mode=save]"],
  [255, 1, "minecraft:structure_block[mode=load]"],
  [255, 2, "minecraft:structure_block[mode=corner]"],
  [255, 3, "minecraft:structure_block[mode=data]"]
]

class BLOCKS(object):
    def __init__(self):
        self.inited=False
        self.blocks_name = []
        self.blocks_mapping_name_id = {}
        self.blocks_mapping_id_name = {}
        self.blocks_mapping_name_description_id_val = defaultdict(lambda: {})
        self.blocks_mapping_name_description_val = defaultdict(lambda: {})
        self.blocks_define=BLOCKS_DEFINE

    def init(self):
        if self.inited:
            return
        else:
            # lazy loading
            self._init()

    def _init(self):
        self.inited=True
        print(
          '''the blocks define is copied from MCEdit 2.0
          MCEdit2.0: https://github.com/mcedit/mcedit2
          LICENSE: https://github.com/mcedit/mcedit2/blob/master/LICENSE.md  '''
        )
        for block_id,block_value,block_full_description in self.blocks_define:
            block_full_description=block_full_description.split(':')[1]
            block_statues_description=None
            block_short_name=None
            div_p=block_full_description.find('[')
            if div_p!=-1:
                block_short_name=block_full_description[:div_p]
                # print(block_short_name)
                block_statues_description=block_full_description[div_p:]
            else:
              block_short_name=block_full_description
            self.blocks_mapping_name_id[block_short_name]=block_id
            self.blocks_mapping_id_name[block_id]=block_short_name

            if block_statues_description:
                block_statues_description=block_statues_description[1:-1]
                block_statues_description=block_statues_description.split(',')
                status=tuple([tuple(desp.split('=')) for desp in block_statues_description])
                self.blocks_mapping_name_description_id_val[block_short_name][status]=(block_id, block_value)
                self.blocks_mapping_name_description_val[block_short_name][status]=block_value
            else:
                self.blocks_mapping_name_description_id_val[block_short_name]=(block_short_name, 0)
                self.blocks_mapping_name_description_val[block_short_name]=0
        for block_id in range(256):
            block_name=self.blocks_mapping_id_name.get(block_id)
            if block_name is not None:
                self.blocks_name.append(block_name)
    @property
    def defines(self):
        return self.blocks_define

    @property
    def names(self):
        self.init()
        return self.blocks_name

    @property
    def name_id_mapping(self):
        self.init()
        return self.blocks_mapping_name_id

    @property
    def id_name_mapping(self):
        self.init()
        return self.blocks_mapping_id_name

    @property
    def name_description_id_val_mapping(self):
        self.init()
        return self.blocks_mapping_name_description_id_val

    @property
    def name_description_val_mapping(self):
        self.init()
        return self.blocks_mapping_name_description_val

blocks=BLOCKS()