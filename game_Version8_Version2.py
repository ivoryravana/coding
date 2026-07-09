"""
Text Adventure Game - A full-featured RPG with battles, shops, quests, crafting, and more.
"""

from enum import Enum
from typing import Dict, List, Optional, Tuple
import random

# ==================== CONSTANTS ====================
class GameState(Enum):
    """Enum for different game states."""
    MENU = "menu"
    TRAVELING = "traveling"
    BATTLE = "battle"
    SHOP = "shop"
    INVENTORY = "inventory"

class Location(Enum):
    """Enum for game locations."""
    VILLAGE = "Village"
    FOREST = "Forest"
    CAVE = "Cave"
    CASTLE = "Castle"
    SWAMP = "Swamp"
    MOUNTAIN = "Mountain"
    DUNGEON = "Dungeon"
    CEMETERY = "Cemetery"

class MenuItem(Enum):
    """Enum for main menu options."""
    TRAVEL = "1"
    SHOP = "2"
    STATS = "3"
    INVENTORY = "4"
    SELL = "5"
    QUESTS = "6"
    MAP = "7"
    PETS = "8"
    CRAFTING = "9"
    ACHIEVEMENTS = "10"
    BESTIARY = "11"
    QUIT = "12"

class ShopItem(Enum):
    """Enum for shop items."""
    SMALL_POTION = "1"
    MEDIUM_POTION = "2"
    LARGE_POTION = "3"
    DAGGER = "4"
    SWORD = "5"
    AXE = "6"
    LEGENDARY_SWORD = "7"
    SHIELD = "8"
    BOOTS = "9"
    BLACKSMITH = "10"
    ENCHANTER = "11"
    PET_SHOP = "12"
    LEAVE = "13"

class Difficulty(Enum):
    """Enum for game difficulty."""
    EASY = "easy"
    NORMAL = "normal"
    HARD = "hard"

class StatusEffect(Enum):
    """Enum for status effects."""
    POISON = "poison"
    STUN = "stun"
    BURN = "burn"
    BLEEDING = "bleeding"

class Enchantment(Enum):
    """Enum for enchantments."""
    FIRE = "fire"
    POISON = "poison"
    LIFESTEAL = "lifesteal"
    CRITICAL = "critical"

class TimeOfDay(Enum):
    """Enum for time of day."""
    DAY = "day"
    NIGHT = "night"

# ==================== ITEM DATA ====================
SHOP_ITEMS = {
    "Small Potion": {"price": 10, "effect": "health", "value": 20, "rarity": "common"},
    "Medium Potion": {"price": 20, "effect": "health", "value": 40, "rarity": "common"},
    "Large Potion": {"price": 35, "effect": "health", "value": 60, "rarity": "common"},
    "Dagger": {"price": 25, "effect": "offense", "value": 5, "rarity": "common"},
    "Sword": {"price": 40, "effect": "offense", "value": 10, "rarity": "uncommon"},
    "Axe": {"price": 55, "effect": "offense", "value": 15, "rarity": "uncommon"},
    "Legendary Sword": {"price": 150, "effect": "offense", "value": 25, "rarity": "legendary"},
    "Shield": {"price": 50, "effect": "defense", "value": 0.15, "rarity": "uncommon"},
    "Boots": {"price": 30, "effect": "dodge", "value": 0.20, "rarity": "uncommon"},
    "Armor": {"price": 40, "effect": "health", "value": 25, "rarity": "uncommon"},
}

SELLABLE_ITEMS = {
    "Wolf Pelt": 15,
    "Goblin Ear": 20,
    "Dragon Scale": 100,
    "Orc Fang": 25,
    "Spider Silk": 18,
    "Bat Wing": 12,
    "Skeleton Bone": 22,
    "Ruby": 40,
    "Emerald": 50,
    "Diamond": 75,
    "Gold Coin": 10,
    "Magic Ring": 200,
    "Shadow Scale": 120,
}

TREASURES = ["Ruby", "Emerald", "Diamond", "Gold Coin"]
CURSED_TREASURES = ["Cursed Amulet", "Cursed Ring"]

ANIMAL_DROPS = {
    "Wolf": "Wolf Pelt",
    "Goblin": "Goblin Ear",
    "Dragon": "Dragon Scale",
    "Orc": "Orc Fang",
    "Giant Spider": "Spider Silk",
    "Bat": "Bat Wing",
    "Skeleton": "Skeleton Bone",
    "Undead Knight": "Skeleton Bone",
    "Shadow Beast": "Shadow Scale",
}

CRAFTING_RECIPES = {
    "Healing Salve": {
        "ingredients": {"Bat Wing": 2, "Emerald": 1},
        "result": "Healing Salve",
        "price": 50,
        "level": 1,
        "effect": "health",
        "value": 50,
    },
    "Fire Bomb": {
        "ingredients": {"Dragon Scale": 1, "Ruby": 2},
        "result": "Fire Bomb",
        "price": 75,
        "level": 5,
        "effect": "special",
        "value": 30,  # Damage
    },
    "Antidote": {
        "ingredients": {"Spider Silk": 3, "Skeleton Bone": 1},
        "result": "Antidote",
        "price": 60,
        "level": 3,
        "effect": "cure_poison",
        "value": 1,
    },
    "Mana Potion": {
        "ingredients": {"Diamond": 1, "Gold Coin": 3},
        "result": "Mana Potion",
        "price": 100,
        "level": 7,
        "effect": "special",
        "value": 40,
    },
    "Shadow Cloak": {
        "ingredients": {"Shadow Scale": 2, "Emerald": 1, "Spider Silk": 3},
        "result": "Shadow Cloak",
        "price": 150,
        "level": 10,
        "effect": "defense",
        "value": 0.25,
    },
}

PET_TYPES = {
    "Wolf Pup": {
        "price": 100,
        "health": 30,
        "damage": (3, 8),
        "xp_bonus": 1.1,
        "description": "A young wolf companion",
    },
    "Dragon Hatchling": {
        "price": 200,
        "health": 50,
        "damage": (5, 12),
        "xp_bonus": 1.25,
        "description": "A baby dragon",
    },
    "Phoenix": {
        "price": 300,
        "health": 40,
        "damage": (6, 14),
        "xp_bonus": 1.3,
        "description": "A legendary phoenix",
    },
}

ENCHANTMENTS = {
    "Fire": {"price": 50, "effect": "fire_damage", "damage_bonus": (3, 6)},
    "Poison": {"price": 40, "effect": "poison_damage", "poison_chance": 0.2},
    "Lifesteal": {"price": 60, "effect": "lifesteal", "heal_percent": 0.25},
    "Critical": {"price": 45, "effect": "critical_boost", "crit_bonus": 0.15},
}

ACHIEVEMENTS = {
    "First Blood": {
        "description": "Defeat your first enemy",
        "condition": "enemies_killed >= 1",
        "reward_gold": 50,
        "unlocked": False,
    },
    "Beast Slayer": {
        "description": "Defeat 10 enemies",
        "condition": "enemies_killed >= 10",
        "reward_gold": 100,
        "unlocked": False,
    },
    "Legendary Hunter": {
        "description": "Defeat 50 enemies",
        "condition": "enemies_killed >= 50",
        "reward_gold": 250,
        "unlocked": False,
    },
    "Damage Dealer": {
        "description": "Deal 1000 damage in total",
        "condition": "total_damage >= 1000",
        "reward_gold": 150,
        "unlocked": False,
    },
    "Tank": {
        "description": "Survive 1000 damage taken",
        "condition": "total_damage_taken >= 1000",
        "reward_gold": 150,
        "unlocked": False,
    },
    "Rich": {
        "description": "Collect 500 gold",
        "condition": "gold >= 500",
        "reward_gold": 100,
        "unlocked": False,
    },
    "Treasure Hunter": {
        "description": "Collect 10 treasures",
        "condition": "treasures >= 10",
        "reward_gold": 200,
        "unlocked": False,
    },
    "Quest Master": {
        "description": "Complete 3 quests",
        "condition": "quests_completed >= 3",
        "reward_gold": 200,
        "unlocked": False,
    },
    "Leveled Up": {
        "description": "Reach level 10",
        "condition": "level >= 10",
        "reward_gold": 300,
        "unlocked": False,
    },
    "Ultimate Warrior": {
        "description": "Reach level 20",
        "condition": "level >= 20",
        "reward_gold": 500,
        "unlocked": False,
    },
}

DIFFICULTY_MULTIPLIERS = {
    Difficulty.EASY: {"health": 0.7, "damage": 0.7, "gold": 1.5, "starting_gold": 50},
    Difficulty.NORMAL: {"health": 1.0, "damage": 1.0, "gold": 1.0, "starting_gold": 20},
    Difficulty.HARD: {"health": 1.3, "damage": 1.3, "gold": 0.8, "starting_gold": 10},
}

ENEMY_DATA = {
    Location.FOREST: [
        {"name": "Wolf", "health": 30, "damage_range": (5, 18), "xp": 50, "boss": False},
        {"name": "Wild Boar", "health": 35, "damage_range": (6, 15), "xp": 55, "boss": False},
    ],
    Location.CAVE: [
        {"name": "Goblin", "health": 45, "damage_range": (12, 25), "xp": 80, "boss": False},
        {"name": "Orc", "health": 55, "damage_range": (15, 28), "xp": 100, "boss": False},
        {"name": "Goblin King", "health": 80, "damage_range": (18, 35), "xp": 200, "boss": True},
    ],
    Location.CASTLE: [
        {"name": "Dragon", "health": 80, "damage_range": (20, 35), "xp": 250, "boss": False},
    ],
    Location.SWAMP: [
        {"name": "Giant Spider", "health": 40, "damage_range": (10, 22), "xp": 70, "boss": False},
        {"name": "Swamp Troll", "health": 60, "damage_range": (14, 26), "xp": 120, "boss": False},
    ],
    Location.MOUNTAIN: [
        {"name": "Mountain Goat", "health": 25, "damage_range": (4, 12), "xp": 40, "boss": False},
        {"name": "Rock Elemental", "health": 70, "damage_range": (18, 32), "xp": 180, "boss": True},
    ],
    Location.DUNGEON: [
        {"name": "Bat", "health": 20, "damage_range": (3, 10), "xp": 30, "boss": False},
        {"name": "Skeleton", "health": 35, "damage_range": (8, 18), "xp": 75, "boss": False},
        {"name": "Undead Knight", "health": 90, "damage_range": (22, 38), "xp": 300, "boss": True},
    ],
    Location.CEMETERY: [
        {"name": "Ghost", "health": 30, "damage_range": (7, 16), "xp": 65, "boss": False},
        {"name": "Shadow Beast", "health": 75, "damage_range": (20, 36), "xp": 220, "boss": True},
    ],
}

NIGHT_ENEMIES = {
    Location.FOREST: [
        {"name": "Shadow Wolf", "health": 40, "damage_range": (8, 20), "xp": 70, "boss": False},
    ],
    Location.SWAMP: [
        {"name": "Swamp Wraith", "health": 50, "damage_range": (12, 25), "xp": 90, "boss": False},
    ],
    Location.CEMETERY: [
        {"name": "Vampire", "health": 80, "damage_range": (18, 32), "xp": 200, "boss": True},
    ],
}

FINAL_BOSS_DATA = {"name": "Shadow Lord", "health": 150, "damage_range": (25, 45), "xp": 500}

QUESTS = {
    "wolf_slayer": {
        "name": "Wolf Slayer",
        "description": "Defeat 3 wolves",
        "target": "Wolf",
        "count": 3,
        "reward_gold": 100,
        "reward_xp": 150,
    },
    "goblin_hunter": {
        "name": "Goblin Hunter",
        "description": "Defeat 5 goblins",
        "target": "Goblin",
        "count": 5,
        "reward_gold": 150,
        "reward_xp": 200,
    },
    "treasure_collector": {
        "name": "Treasure Collector",
        "description": "Collect 5 treasures",
        "target": "treasure",
        "count": 5,
        "reward_gold": 200,
        "reward_xp": 250,
    },
    "dragon_slayer": {
        "name": "Dragon Slayer",
        "description": "Defeat a dragon",
        "target": "Dragon",
        "count": 1,
        "reward_gold": 300,
        "reward_xp": 400,
    },
}

SKILL_TREES = {
    "warrior": {
        "name": "Warrior",
        "level_1": {"offense": 5, "health": 10},
        "level_5": {"offense": 15, "health": 30},
        "level_10": {"offense": 30, "health": 60, "ability": "Power Strike (2x damage)"},
    },
    "rogue": {
        "name": "Rogue",
        "level_1": {"dodge": 0.10, "offense": 3},
        "level_5": {"dodge": 0.25, "offense": 10},
        "level_10": {"dodge": 0.40, "offense": 20, "ability": "Shadow Clone (avoid damage)"},
    },
    "paladin": {
        "name": "Paladin",
        "level_1": {"defense": 0.10, "health": 15},
        "level_5": {"defense": 0.25, "health": 40},
        "level_10": {"defense": 0.40, "health": 70, "ability": "Holy Shield (reduce all damage)"},
    },
}

LOCATION_CONNECTIONS = {
    Location.VILLAGE: [Location.FOREST, Location.CAVE, Location.CASTLE],
    Location.FOREST: [Location.VILLAGE, Location.SWAMP, Location.MOUNTAIN],
    Location.CAVE: [Location.VILLAGE, Location.DUNGEON],
    Location.CASTLE: [Location.VILLAGE],
    Location.SWAMP: [Location.FOREST, Location.CEMETERY],
    Location.MOUNTAIN: [Location.FOREST, Location.DUNGEON],
    Location.DUNGEON: [Location.CAVE, Location.MOUNTAIN],
    Location.CEMETERY: [Location.SWAMP],
}

TRAVELS_TO_FINAL_BOSS = 30
MAX_HEALTH = 100
MAX_LEVEL = 20
HARDCORE_MODE = False

# ==================== PET CLASS ====================
class Pet:
    """Represents a companion pet."""

    def __init__(self, pet_type: str):
        """Initialize a pet."""
        self.pet_type = pet_type
        self.data = PET_TYPES[pet_type]
        self.health = self.data["health"]
        self.max_health = self.data["health"]
        self.level = 1
        self.xp = 0

    def take_damage(self, damage: int) -> None:
        """Reduce pet health."""
        self.health = max(0, self.health - damage)

    def heal(self, amount: int) -> None:
        """Heal pet."""
        self.health = min(self.max_health, self.health + amount)

    def is_alive(self) -> bool:
        """Check if pet is alive."""
        return self.health > 0

    def get_damage(self) -> int:
        """Get pet damage."""
        return random.randint(*self.data["damage"])

    def level_up(self) -> None:
        """Level up pet."""
        self.level += 1
        self.max_health += 10
        self.health = self.max_health

# ==================== PLAYER CLASS ====================
class Player:
    """Represents the player character."""

    def __init__(self, name: str, difficulty: Difficulty):
        """Initialize a player with default stats."""
        self.name = name
        self.difficulty = difficulty
        self.health = MAX_HEALTH
        self.max_health = MAX_HEALTH
        self.gold = DIFFICULTY_MULTIPLIERS[difficulty]["starting_gold"]
        self.inventory: List[str] = ["Torch"]
        self.enchanted_items: Dict[str, str] = {}
        self.location = Location.VILLAGE
        self.offense = 10
        self.defense = 0.0
        self.dodge = 0.0
        self.travel_count = 0
        self.level = 1
        self.xp = 0
        self.xp_to_level = 100
        self.skill_tree = None
        self.status_effects: Dict[StatusEffect, int] = {}
        self.active_quests: Dict[str, int] = {}
        self.completed_quests: List[str] = []
        self.enemies_defeated: Dict[str, int] = {}
        self.treasures_collected = 0
        self.total_damage_dealt = 0
        self.total_damage_taken = 0
        self.battles_won = 0
        self.battles_lost = 0
        self.pet: Optional[Pet] = None
        self.bestiary: Dict[str, Dict] = {}
        self.time_of_day = TimeOfDay.DAY
        self.crafted_items: Dict[str, int] = {}
        self.talents: List[str] = []
        self.hardcore_mode = HARDCORE_MODE
        self.prestige_level = 0
        self.prestige_bonuses = {}
        self.mystery_boxes_opened = 0

    def take_damage(self, damage: int) -> None:
        """Reduce health by damage amount."""
        reduced_damage = int(damage * (1 - self.defense))
        self.health = max(0, self.health - reduced_damage)
        self.total_damage_taken += reduced_damage

    def heal(self, amount: int) -> None:
        """Increase health up to max."""
        self.health = min(self.max_health, self.health + amount)

    def add_gold(self, amount: int) -> None:
        """Add gold to inventory."""
        multiplier = DIFFICULTY_MULTIPLIERS[self.difficulty]["gold"]
        self.gold += int(amount * multiplier)

    def spend_gold(self, amount: int) -> bool:
        """Attempt to spend gold. Returns True if successful."""
        if self.gold >= amount:
            self.gold -= amount
            return True
        return False

    def add_item(self, item: str) -> None:
        """Add item to inventory."""
        self.inventory.append(item)
        if item in SELLABLE_ITEMS:
            self.treasures_collected += 1

    def remove_item(self, item: str) -> bool:
        """Remove item from inventory. Returns True if successful."""
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False

    def increase_offense(self, amount: int) -> None:
        """Increase offense stat."""
        self.offense += amount

    def increase_defense(self, amount: float) -> None:
        """Increase defense stat."""
        self.defense = min(0.80, self.defense + amount)

    def increase_dodge(self, amount: float) -> None:
        """Increase dodge stat."""
        self.dodge = min(0.50, self.dodge + amount)

    def increase_max_health(self, amount: int) -> None:
        """Increase max health (permanently)."""
        self.max_health += amount
        self.health = min(self.health + amount, self.max_health)

    def gain_xp(self, amount: int) -> None:
        """Gain experience points."""
        if self.pet:
            pet_bonus = self.pet.data["xp_bonus"]
            amount = int(amount * pet_bonus)
        
        self.xp += amount
        if self.pet:
            self.pet.xp += amount
            if self.pet.xp >= 200:
                self.pet.level_up()
                self.pet.xp = 0
        
        while self.xp >= self.xp_to_level and self.level < MAX_LEVEL:
            self.level_up()

    def level_up(self) -> None:
        """Level up the player."""
        self.xp -= self.xp_to_level
        self.level += 1
        self.xp_to_level = int(self.xp_to_level * 1.2)
        self.offense += 2
        self.max_health += 10
        self.health = self.max_health
        
        # Apply talent bonuses every 2 levels
        if self.level % 2 == 0:
            self.apply_talent_bonus()

    def apply_talent_bonus(self) -> None:
        """Apply passive talent bonuses."""
        if self.skill_tree == "warrior":
            self.increase_offense(1)
            self.increase_max_health(5)
        elif self.skill_tree == "rogue":
            self.increase_dodge(0.05)
            self.increase_offense(2)
        elif self.skill_tree == "paladin":
            self.increase_defense(0.05)
            self.increase_max_health(8)

    def add_status_effect(self, effect: StatusEffect, duration: int) -> None:
        """Add a status effect."""
        self.status_effects[effect] = duration

    def apply_status_effects(self) -> None:
        """Apply status effects each turn."""
        if StatusEffect.POISON in self.status_effects:
            self.take_damage(5)
            self.status_effects[StatusEffect.POISON] -= 1
            if self.status_effects[StatusEffect.POISON] <= 0:
                del self.status_effects[StatusEffect.POISON]

        if StatusEffect.BURN in self.status_effects:
            self.take_damage(8)
            self.status_effects[StatusEffect.BURN] -= 1
            if self.status_effects[StatusEffect.BURN] <= 0:
                del self.status_effects[StatusEffect.BURN]

        if StatusEffect.BLEEDING in self.status_effects:
            self.take_damage(3)
            self.status_effects[StatusEffect.BLEEDING] -= 1
            if self.status_effects[StatusEffect.BLEEDING] <= 0:
                del self.status_effects[StatusEffect.BLEEDING]

    def travel(self) -> None:
        """Increment travel count."""
        self.travel_count += 1
        self.time_of_day = TimeOfDay.NIGHT if random.random() < 0.5 else TimeOfDay.DAY

    def choose_skill_tree(self, tree_name: str) -> None:
        """Choose a skill tree."""
        self.skill_tree = tree_name
        tree = SKILL_TREES[tree_name]
        bonuses = tree.get("level_1", {})
        if "offense" in bonuses:
            self.increase_offense(bonuses["offense"])
        if "health" in bonuses:
            self.increase_max_health(bonuses["health"])
        if "defense" in bonuses:
            self.increase_defense(bonuses["defense"])
        if "dodge" in bonuses:
            self.increase_dodge(bonuses["dodge"])

    def apply_skill_bonuses(self) -> None:
        """Apply bonuses based on current level."""
        if not self.skill_tree:
            return

        tree = SKILL_TREES[self.skill_tree]
        if self.level >= 5 and self.level < 10:
            bonuses = tree.get("level_5", {})
            if "level_5_applied" not in self.__dict__:
                self.level_5_applied = True
                if "offense" in bonuses:
                    self.increase_offense(bonuses["offense"])
                if "health" in bonuses:
                    self.increase_max_health(bonuses["health"])
                if "defense" in bonuses:
                    self.increase_defense(bonuses["defense"])
                if "dodge" in bonuses:
                    self.increase_dodge(bonuses["dodge"])

        if self.level >= 10:
            bonuses = tree.get("level_10", {})
            if "level_10_applied" not in self.__dict__:
                self.level_10_applied = True
                if "offense" in bonuses:
                    self.increase_offense(bonuses["offense"])
                if "health" in bonuses:
                    self.increase_max_health(bonuses["health"])
                if "defense" in bonuses:
                    self.increase_defense(bonuses["defense"])
                if "dodge" in bonuses:
                    self.increase_dodge(bonuses["dodge"])

    def update_quest_progress(self, enemy_name: str) -> None:
        """Update quest progress when defeating an enemy."""
        for quest_id, quest in QUESTS.items():
            if quest_id not in self.active_quests:
                continue
            if quest["target"] == enemy_name:
                self.active_quests[quest_id] += 1

    def update_treasure_quest(self) -> None:
        """Update treasure quest progress."""
        for quest_id, quest in QUESTS.items():
            if quest_id not in self.active_quests:
                continue
            if quest["target"] == "treasure":
                self.active_quests[quest_id] += 1

    def add_to_bestiary(self, enemy_name: str, enemy: 'Enemy') -> None:
        """Add enemy to bestiary."""
        if enemy_name not in self.bestiary:
            self.bestiary[enemy_name] = {
                "name": enemy.name,
                "health": enemy.base_health,
                "damage": enemy.damage_range,
                "xp": enemy.xp,
                "is_boss": enemy.is_boss,
                "encounters": 0,
            }
        self.bestiary[enemy_name]["encounters"] += 1

    def check_achievements(self) -> None:
        """Check and unlock achievements."""
        enemies_killed = sum(self.enemies_defeated.values())
        
        for ach_name, achievement in ACHIEVEMENTS.items():
            if achievement["unlocked"]:
                continue
            
            condition = achievement["condition"]
            if "enemies_killed" in condition:
                target = int(condition.split()[-1])
                if enemies_killed >= target:
                    achievement["unlocked"] = True
                    self.add_gold(achievement["reward_gold"])
                    print(f"\n  🏆 ACHIEVEMENT UNLOCKED: {ach_name}!")
            elif "total_damage" in condition:
                target = int(condition.split()[-1])
                if self.total_damage_dealt >= target:
                    achievement["unlocked"] = True
                    self.add_gold(achievement["reward_gold"])
                    print(f"\n  🏆 ACHIEVEMENT UNLOCKED: {ach_name}!")
            elif "total_damage_taken" in condition:
                target = int(condition.split()[-1])
                if self.total_damage_taken >= target:
                    achievement["unlocked"] = True
                    self.add_gold(achievement["reward_gold"])
                    print(f"\n  🏆 ACHIEVEMENT UNLOCKED: {ach_name}!")
            elif "gold" in condition:
                target = int(condition.split()[-1])
                if self.gold >= target:
                    achievement["unlocked"] = True
                    self.add_gold(achievement["reward_gold"])
                    print(f"\n  🏆 ACHIEVEMENT UNLOCKED: {ach_name}!")
            elif "treasures" in condition:
                target = int(condition.split()[-1])
                if self.treasures_collected >= target:
                    achievement["unlocked"] = True
                    self.add_gold(achievement["reward_gold"])
                    print(f"\n  🏆 ACHIEVEMENT UNLOCKED: {ach_name}!")
            elif "quests_completed" in condition:
                target = int(condition.split()[-1])
                if len(self.completed_quests) >= target:
                    achievement["unlocked"] = True
                    self.add_gold(achievement["reward_gold"])
                    print(f"\n  🏆 ACHIEVEMENT UNLOCKED: {ach_name}!")
            elif "level" in condition:
                target = int(condition.split()[-1])
                if self.level >= target:
                    achievement["unlocked"] = True
                    self.add_gold(achievement["reward_gold"])
                    print(f"\n  🏆 ACHIEVEMENT UNLOCKED: {ach_name}!")

# ==================== ENEMY CLASS ====================
class Enemy:
    """Represents an enemy in battle."""

    def __init__(self, name: str, health: int, damage_range: tuple, xp: int = 0, is_boss: bool = False):
        """Initialize an enemy with stats."""
        self.name = name
        self.base_health = health
        self.health = health
        self.damage_range = damage_range
        self.xp = xp
        self.is_boss = is_boss
        self.abilities = self._get_abilities()
        self.weaknesses = self._get_weaknesses()

    def _get_abilities(self) -> List[str]:
        """Get special abilities based on enemy type."""
        abilities = {
            "Dragon": ["Fire Breath", "Tail Sweep"],
            "Goblin King": ["Summon Minions", "Poison Spit"],
            "Rock Elemental": ["Stone Throw", "Earthquake"],
            "Undead Knight": ["Drain Life", "Cursed Strike"],
            "Shadow Beast": ["Shadow Merge", "Dark Aura"],
            "Vampire": ["Life Drain", "Shadow Step"],
            "Shadow Wolf": ["Pack Attack", "Howl"],
        }
        return abilities.get(self.name, [])

    def _get_weaknesses(self) -> List[str]:
        """Get enemy weaknesses."""
        weaknesses = {
            "Dragon": ["Cold", "Water"],
            "Fire Elemental": ["Water"],
            "Ghost": ["Holy", "Silver"],
            "Undead": ["Holy", "Fire"],
        }
        for weakness_type, weak_list in weaknesses.items():
            if weakness_type in self.name:
                return weak_list
        return []

    def take_damage(self, damage: int) -> None:
        """Reduce health by damage amount."""
        self.health = max(0, self.health - damage)

    def is_alive(self) -> bool:
        """Check if enemy is still alive."""
        return self.health > 0

    def heal(self, amount: int) -> None:
        """Enemy heals itself."""
        self.health = min(self.base_health, self.health + amount)

# ==================== DISPLAY FUNCTIONS ====================
def display_menu() -> None:
    """Display the main menu."""
    print("\n" + "="*40)
    print("       MAIN MENU")
    print("="*40)
    print("\n  1. Travel")
    print("  2. Shop")
    print("  3. Stats")
    print("  4. Inventory")
    print("  5. Sell Items")
    print("  6. Quests")
    print("  7. Map")
    print("  8. Pets")
    print("  9. Crafting")
    print("  10. Achievements")
    print("  11. Bestiary")
    print("  12. Quit")
    print("\n" + "="*40)

def display_player_stats(player: Player) -> None:
    """Display player statistics."""
    print("\n" + "="*40)
    print("       PLAYER STATS")
    print("="*40)
    print(f"\n  Name:              {player.name}")
    print(f"  Level:             {player.level} / {MAX_LEVEL}")
    print(f"  Health:            {player.health} / {player.max_health}")
    print(f"  Gold:              {player.gold}")
    print(f"  Location:          {player.location.value}")
    print(f"  Time:              {player.time_of_day.value.capitalize()}")
    print(f"  Offense:           {player.offense}")
    print(f"  Defense:           {int(player.defense * 100)}%")
    print(f"  Dodge:             {int(player.dodge * 100)}%")
    print(f"  Experience:        {player.xp} / {player.xp_to_level}")
    print(f"\n  Skill Tree:        {player.skill_tree if player.skill_tree else 'None'}")
    print(f"  Difficulty:        {player.difficulty.value.capitalize()}")
    
    if player.pet:
        print(f"  Pet:               {player.pet.pet_type} (Lvl {player.pet.level})")
        print(f"  Pet Health:        {player.pet.health} / {player.pet.max_health}")
    
    print(f"\n  Statistics:")
    print(f"    • Battles Won:     {player.battles_won}")
    print(f"    • Enemies Killed:  {sum(player.enemies_defeated.values())}")
    print(f"    • Damage Dealt:    {player.total_damage_dealt}")
    print(f"    • Damage Taken:    {player.total_damage_taken}")
    print(f"    • Treasures:       {player.treasures_collected}")
    print(f"    • Prestige Level:  {player.prestige_level}")
    
    if player.status_effects:
        print(f"\n  Status Effects:")
        for effect, duration in player.status_effects.items():
            print(f"    • {effect.value.capitalize()} ({duration} turns)")
    
    print("\n" + "="*40)

def display_inventory(player: Player) -> None:
    """Display inventory with prices for sellable items."""
    print("\n" + "="*40)
    print("       YOUR INVENTORY")
    print("="*40 + "\n")
    
    if not player.inventory:
        print("  (empty)")
    else:
        for item in player.inventory:
            if item in SELLABLE_ITEMS:
                enchant = ""
                if item in player.enchanted_items:
                    enchant = f" ✨ ({player.enchanted_items[item]})"
                print(f"  • {item:<20} ({SELLABLE_ITEMS[item]} gold){enchant}")
            elif item in CURSED_TREASURES:
                print(f"  • {item:<20} ⚠️ (CURSED - needs priest)")
            elif item in CRAFTING_RECIPES:
                print(f"  • {item:<20} (Crafted)")
            else:
                print(f"  • {item}")
    
    print("\n" + "="*40)

def display_locations(player: Player) -> None:
    """Display available locations to travel to."""
    print("\n" + "-"*40)
    print(f"  Current Location: {player.location.value}")
    print(f"  Time: {player.time_of_day.value.capitalize()}")
    print("-"*40)
    print("\n  Connected Locations:\n")
    
    if player.location in LOCATION_CONNECTIONS:
        for i, location in enumerate(LOCATION_CONNECTIONS[player.location], 1):
            print(f"  {i}. {location.value}")

def display_shop_menu(player: Player) -> None:
    """Display the shop menu."""
    print("\n" + "="*40)
    print("       SHOP")
    print("="*40)
    print(f"\n  Gold: {player.gold}\n")
    
    print("  POTIONS:")
    print("  1. Small Potion (10 gold) - +20 health")
    print("  2. Medium Potion (20 gold) - +40 health")
    print("  3. Large Potion (35 gold) - +60 health\n")
    
    print("  WEAPONS:")
    print("  4. Dagger (25 gold) - +5 offense")
    print("  5. Sword (40 gold) - +10 offense")
    print("  6. Axe (55 gold) - +15 offense")
    print("  7. Legendary Sword (150 gold) - +25 offense\n")
    
    print("  ARMOR & ACCESSORIES:")
    print("  8. Shield (50 gold) - +15% defense")
    print("  9. Boots (30 gold) - +20% dodge")
    print("  10. Armor (40 gold) - +25 health\n")
    
    print("  SERVICES:")
    print("  11. Visit Blacksmith (upgrade items)")
    print("  12. Visit Enchanter (enchant items)")
    print("  13. Visit Pet Shop (adopt a pet)")
    print("  14. Leave")
    print("\n" + "="*40)

def display_battle_start(enemy: Enemy, time_of_day: TimeOfDay) -> None:
    """Display battle start message."""
    print("\n" + "="*40)
    print("       BATTLE START!")
    print("="*40)
    badge = "👑 BOSS" if enemy.is_boss else ""
    print(f"\n  ⚔️  A {enemy.name} attacks you! {badge}")
    print(f"\n  {enemy.name} Health: {enemy.health}")
    if enemy.abilities:
        print(f"  Special Abilities: {', '.join(enemy.abilities)}")
    if enemy.weaknesses:
        print(f"  Weaknesses: {', '.join(enemy.weaknesses)}")
    if time_of_day == TimeOfDay.NIGHT:
        print(f"  🌙 This battle takes place at NIGHT!")
    print("\n" + "-"*40)

def display_damage_dealt(damage: int, critical: bool = False, enchantment: str = None) -> None:
    """Display damage dealt to enemy."""
    msg = ""
    if enchantment == "fire":
        msg = f"\n  🔥 FIRE DAMAGE! You deal {damage} damage!"
    elif enchantment == "poison":
        msg = f"\n  ☠️ POISON DAMAGE! You deal {damage} damage!"
    elif critical:
        msg = f"\n  ⚡ CRITICAL HIT! You deal {damage} damage!"
    else:
        msg = f"\n  ✓ You deal {damage} damage!"
    
    print(msg)

def display_damage_taken(enemy: Enemy, damage: int, player_health: int) -> None:
    """Display damage taken from enemy."""
    print(f"\n  ✗ The {enemy.name} hits you for {damage} damage!")
    print(f"    Your health: {player_health} / {player_health + damage}")

def display_enemy_defeated(enemy: Enemy, gold: int, item: str) -> None:
    """Display victory message and rewards."""
    print("\n" + "="*40)
    print("       VICTORY!")
    print("="*40)
    print(f"\n  ✨ You defeated the {enemy.name}!")
    print(f"\n  Rewards:")
    print(f"    • {gold} gold")
    print(f"    • {item}")
    print(f"    • {enemy.xp} XP")

def display_enemy_drop(enemy: Enemy, drop: str) -> None:
    """Display enemy drop."""
    print(f"    • {drop} (dropped by {enemy.name})")

def display_ran_away(enemy: Enemy) -> None:
    """Display flee message."""
    print(f"\n  🏃 You ran away from the {enemy.name}!")
    print("\n" + "-"*40)

def display_cannot_escape() -> None:
    """Display cannot escape message."""
    print("\n  ⛔ You cannot escape the Shadow Lord!")

def display_final_boss_arrival() -> None:
    """Display final boss arrival."""
    print("\n" + "█"*40)
    print("  ⚠️  A SHADOW FALLS OVER THE LAND...")
    print("█"*40)
    print("\n  The Shadow Lord emerges from the darkness!")
    print("\n" + "█"*40)

def display_victory() -> None:
    """Display victory message."""
    print("\n" + "★"*40)
    print("  ✨ YOU HAVE DEFEATED THE SHADOW LORD! ✨")
    print("★"*40)
    print("\n  The land is saved!")
    print("\n  YOU WIN!")
    print("\n" + "★"*40)

def display_game_over(reason: str = "") -> None:
    """Display game over message."""
    print("\n" + "✗"*40)
    print("       GAME OVER!")
    print("✗"*40)
    if reason:
        print(f"\n  {reason}")
    print("\n" + "✗"*40)

def display_travel_info(player: Player) -> None:
    """Display travel count and remaining travels."""
    remaining = TRAVELS_TO_FINAL_BOSS - player.travel_count
    print(f"\n  ➜ Travels until final boss: {remaining}")
    print("-"*40)

def display_map(player: Player) -> None:
    """Display a simple ASCII map."""
    print("\n" + "="*40)
    print("       WORLD MAP")
    print("="*40 + "\n")
    
    map_display = {
        Location.VILLAGE: "🏘️ Village (start)",
        Location.FOREST: "🌲 Forest",
        Location.CAVE: "🕳️ Cave",
        Location.CASTLE: "🏰 Castle",
        Location.SWAMP: "💧 Swamp",
        Location.MOUNTAIN: "⛰️ Mountain",
        Location.DUNGEON: "🏚️ Dungeon",
        Location.CEMETERY: "⚰️ Cemetery",
    }
    
    for location, description in map_display.items():
        marker = "→ " if location == player.location else "  "
        print(f"  {marker}{description}")
    
    print("\n" + "="*40)

def display_quests(player: Player) -> None:
    """Display quests."""
    print("\n" + "="*40)
    print("       QUESTS")
    print("="*40 + "\n")
    
    print("  Active Quests:")
    if not player.active_quests:
        print("    (none)")
    else:
        for quest_id, progress in player.active_quests.items():
            quest = QUESTS[quest_id]
            print(f"\n    • {quest['name']}")
            print(f"      {quest['description']}")
            print(f"      Progress: {progress} / {quest['count']}")
            print(f"      Reward: {quest['reward_gold']} gold, {quest['reward_xp']} XP")
    
    print("\n  Available Quests:")
    for quest_id, quest in QUESTS.items():
        if quest_id not in player.active_quests and quest_id not in player.completed_quests:
            print(f"\n    • {quest['name']}")
            print(f"      {quest['description']}")
    
    if player.completed_quests:
        print("\n  Completed Quests:")
        for quest_id in player.completed_quests:
            quest = QUESTS[quest_id]
            print(f"    ✓ {quest['name']}")
    
    print("\n" + "="*40)

def display_level_up(player: Player) -> None:
    """Display level up message."""
    print("\n" + "⭐"*20)
    print(f"\n  LEVEL UP! You are now level {player.level}!")
    print(f"  Health increased to {player.max_health}")
    print(f"  Offense increased to {player.offense}")
    print("\n" + "⭐"*20 + "\n")

def display_curse_warning(item: str) -> None:
    """Display curse warning."""
    print(f"\n  ⚠️ WARNING! {item} is cursed!")
    print("     You will take damage each turn until cured by a priest.")

def display_skill_tree_selection() -> None:
    """Display skill tree selection menu."""
    print("\n" + "="*40)
    print("       CHOOSE YOUR PATH")
    print("="*40 + "\n")
    
    print("  1. Warrior")
    print("     • Increased Offense")
    print("     • Increased Health")
    print("     • Level 10: Power Strike (2x damage)\n")
    
    print("  2. Rogue")
    print("     • Increased Dodge")
    print("     • Increased Offense")
    print("     • Level 10: Shadow Clone (avoid damage)\n")
    
    print("  3. Paladin")
    print("     • Increased Defense")
    print("     • Increased Health")
    print("     • Level 10: Holy Shield (reduce all damage)\n")
    
    print("="*40)

def display_pets(player: Player) -> None:
    """Display pet management."""
    print("\n" + "="*40)
    print("       PETS")
    print("="*40 + "\n")
    
    if player.pet:
        print(f"  Your Pet: {player.pet.pet_type}")
        print(f"  Level:    {player.pet.level}")
        print(f"  Health:   {player.pet.health} / {player.pet.max_health}")
        print(f"  Damage:   {player.pet.data['damage']}")
        print(f"  XP Bonus: {int((player.pet.data['xp_bonus'] - 1) * 100)}%")
        print(f"\n  1. Release Pet")
        print(f"  2. Back to menu")
    else:
        print("  You don't have a pet.")
        print("\n  1. Back to menu")
    
    print("\n" + "="*40)

def display_crafting_menu(player: Player) -> None:
    """Display crafting menu."""
    print("\n" + "="*40)
    print("       CRAFTING")
    print("="*40 + "\n")
    
    available_recipes = [recipe for recipe_name, recipe in CRAFTING_RECIPES.items() 
                        if recipe.get("level", 1) <= player.level]
    
    if not available_recipes:
        print("  No recipes available at your level.")
        print("\n" + "="*40)
        return
    
    for i, recipe in enumerate(available_recipes, 1):
        print(f"  {i}. {recipe['result']} (Level {recipe.get('level', 1)} required)")
        print(f"     Ingredients: {', '.join([f'{count} {item}' for item, count in recipe['ingredients'].items()])}")
        print(f"     Reward: {recipe['price']} gold worth\n")
    
    print(f"  {len(available_recipes) + 1}. Back to menu")
    print("\n" + "="*40)

def display_achievements(player: Player) -> None:
    """Display achievements."""
    print("\n" + "="*40)
    print("       ACHIEVEMENTS")
    print("="*40 + "\n")
    
    unlocked = sum(1 for ach in ACHIEVEMENTS.values() if ach["unlocked"])
    total = len(ACHIEVEMENTS)
    
    print(f"  Unlocked: {unlocked} / {total}\n")
    
    for name, achievement in ACHIEVEMENTS.items():
        status = "✓" if achievement["unlocked"] else "✗"
        print(f"  {status} {name}")
        print(f"    {achievement['description']}\n")
    
    print("="*40)

def display_bestiary(player: Player) -> None:
    """Display bestiary."""
    print("\n" + "="*40)
    print("       BESTIARY")
    print("="*40 + "\n")
    
    if not player.bestiary:
        print("  (empty - defeat enemies to discover them)\n")
    else:
        for enemy_name, info in player.bestiary.items():
            print(f"  • {info['name']}")
            print(f"    Health: {info['health']}")
            print(f"    Damage: {info['damage']}")
            print(f"    XP Reward: {info['xp']}")
            print(f"    Boss: {'Yes' if info['is_boss'] else 'No'}")
            print(f"    Encountered: {info['encounters']} times\n")
    
    print("="*40)

# ==================== INPUT FUNCTIONS ====================
def get_valid_choice(options: List[str], prompt: str = "> ") -> str:
    """
    Get a valid choice from user.
    
    Args:
        options: List of valid options
        prompt: Prompt to display
    
    Returns:
        The valid choice made by user
    """
    while True:
        choice = input(f"\n  {prompt} ").strip()
        if choice in options:
            return choice
        print(f"  ⚠️  Invalid choice. Please try again.")

def get_location_choice(player: Player) -> Optional[Location]:
    """
    Get a valid location choice from user.
    
    Returns:
        The chosen location or None if invalid
    """
    display_locations(player)
    
    connected_locations = LOCATION_CONNECTIONS[player.location]
    choice = input(f"\n  Choice: ").strip().title()
    
    try:
        location = Location(choice)
        if location in connected_locations:
            return location
        else:
            print(f"\n  ⚠️  {choice} is not connected to {player.location.value}.")
            return None
    except ValueError:
        print("\n  ⚠️  That location doesn't exist.")
        return None

# ==================== SHOP FUNCTIONS ====================
def purchase_item(player: Player, item_name: str, item_data: Dict) -> bool:
    """
    Purchase an item from the shop.
    
    Args:
        player: The player making the purchase
        item_name: Name of the item to purchase
        item_data: Dictionary with price and effect data
    
    Returns:
        True if purchase successful, False otherwise
    """
    price = item_data["price"]
    
    if not player.spend_gold(price):
        print(f"\n  ⚠️  You can't afford a {item_name}.")
        return False
    
    player.add_item(item_name)
    effect_type = item_data["effect"]
    value = item_data["value"]
    
    if effect_type == "health":
        player.heal(value)
        print(f"\n  ✓ You bought a {item_name}!")
        print(f"    Health: {player.health} / {player.max_health}")
    elif effect_type == "offense":
        player.increase_offense(value)
        print(f"\n  ✓ You bought a {item_name}!")
        print(f"    Offense: {player.offense}")
    elif effect_type == "defense":
        player.increase_defense(value)
        print(f"\n  ✓ You bought a {item_name}!")
        print(f"    Defense: {int(player.defense * 100)}%")
    elif effect_type == "dodge":
        player.increase_dodge(value)
        print(f"\n  ✓ You bought a {item_name}!")
        print(f"    Dodge: {int(player.dodge * 100)}%")
    
    return True

def handle_shop(player: Player) -> None:
    """Handle shop interactions."""
    if player.location != Location.VILLAGE:
        print("\n  ⚠️  There is no shop here.")
        return
    
    display_shop_menu(player)
    choice = get_valid_choice([item.value for item in ShopItem])
    
    if choice == "1":
        purchase_item(player, "Small Potion", SHOP_ITEMS["Small Potion"])
    elif choice == "2":
        purchase_item(player, "Medium Potion", SHOP_ITEMS["Medium Potion"])
    elif choice == "3":
        purchase_item(player, "Large Potion", SHOP_ITEMS["Large Potion"])
    elif choice == "4":
        purchase_item(player, "Dagger", SHOP_ITEMS["Dagger"])
    elif choice == "5":
        purchase_item(player, "Sword", SHOP_ITEMS["Sword"])
    elif choice == "6":
        purchase_item(player, "Axe", SHOP_ITEMS["Axe"])
    elif choice == "7":
        purchase_item(player, "Legendary Sword", SHOP_ITEMS["Legendary Sword"])
    elif choice == "8":
        purchase_item(player, "Shield", SHOP_ITEMS["Shield"])
    elif choice == "9":
        purchase_item(player, "Boots", SHOP_ITEMS["Boots"])
    elif choice == "10":
        purchase_item(player, "Armor", SHOP_ITEMS["Armor"])
    elif choice == "11":
        handle_blacksmith(player)
    elif choice == "12":
        handle_enchanter(player)
    elif choice == "13":
        handle_pet_shop(player)
    
    print("\n" + "="*40)

def handle_blacksmith(player: Player) -> None:
    """Handle blacksmith upgrades."""
    weapons = [item for item in player.inventory if item in 
               ["Dagger", "Sword", "Axe", "Legendary Sword"]]
    
    if not weapons:
        print("\n  ⚠️  You have no weapons to upgrade.")
        return
    
    print("\n  Blacksmith says: 'I can upgrade your weapons!'")
    print("\n  Available weapons:")
    for i, weapon in enumerate(weapons, 1):
        print(f"  {i}. {weapon} (costs 50 gold)")
    print(f"  {len(weapons) + 1}. Leave")
    
    options = [str(i) for i in range(1, len(weapons) + 2)]
    choice = get_valid_choice(options, "Choice:")
    
    if int(choice) == len(weapons) + 1:
        return
    
    weapon = weapons[int(choice) - 1]
    if player.spend_gold(50):
        player.increase_offense(5)
        print(f"\n  ✓ Your {weapon} has been upgraded!")
        print(f"    Offense increased to {player.offense}")
    else:
        print(f"\n  ⚠️  You can't afford to upgrade.")

def handle_enchanter(player: Player) -> None:
    """Handle item enchanting."""
    weapons = [item for item in player.inventory if item in 
               ["Dagger", "Sword", "Axe", "Legendary Sword", "Shield"]]
    
    if not weapons:
        print("\n  ⚠️  You have no items to enchant.")
        return
    
    print("\n  Enchanter says: 'Choose an item to enchant!'")
    print("\n  Your items:")
    for i, weapon in enumerate(weapons, 1):
        enchant_status = f" (has {player.enchanted_items[weapon]})" if weapon in player.enchanted_items else ""
        print(f"  {i}. {weapon}{enchant_status}")
    print(f"  {len(weapons) + 1}. Leave")
    
    options = [str(i) for i in range(1, len(weapons) + 2)]
    choice = get_valid_choice(options, "Choice:")
    
    if int(choice) == len(weapons) + 1:
        return
    
    weapon = weapons[int(choice) - 1]
    
    print("\n  Available Enchantments:")
    for i, (ench_name, ench_data) in enumerate(ENCHANTMENTS.items(), 1):
        print(f"  {i}. {ench_name} ({ench_data['price']} gold)")
    print(f"  {len(ENCHANTMENTS) + 1}. Leave")
    
    ench_options = [str(i) for i in range(1, len(ENCHANTMENTS) + 2)]
    ench_choice = get_valid_choice(ench_options, "Choice:")
    
    if int(ench_choice) == len(ENCHANTMENTS) + 1:
        return
    
    ench_name = list(ENCHANTMENTS.keys())[int(ench_choice) - 1]
    ench_data = ENCHANTMENTS[ench_name]
    
    if player.spend_gold(ench_data["price"]):
        player.enchanted_items[weapon] = ench_name
        print(f"\n  ✓ {weapon} has been enchanted with {ench_name}!")
    else:
        print(f"\n  ⚠️  You can't afford this enchantment.")

def handle_pet_shop(player: Player) -> None:
    """Handle pet adoption."""
    if player.pet:
        print("\n  ⚠️  You already have a pet!")
        return
    
    print("\n  Pet Shop Owner says: 'Looking for a companion?'")
    print("\n  Available Pets:")
    for i, (pet_name, pet_data) in enumerate(PET_TYPES.items(), 1):
        print(f"  {i}. {pet_name} ({pet_data['price']} gold)")
        print(f"     {pet_data['description']}")
        print(f"     Health: {pet_data['health']}, XP Bonus: {int((pet_data['xp_bonus'] - 1) * 100)}%\n")
    
    print(f"  {len(PET_TYPES) + 1}. Leave")
    
    options = [str(i) for i in range(1, len(PET_TYPES) + 2)]
    choice = get_valid_choice(options, "Choice:")
    
    if int(choice) == len(PET_TYPES) + 1:
        return
    
    pet_name = list(PET_TYPES.keys())[int(choice) - 1]
    pet_price = PET_TYPES[pet_name]["price"]
    
    if player.spend_gold(pet_price):
        player.pet = Pet(pet_name)
        print(f"\n  ✓ You adopted a {pet_name}!")
    else:
        print(f"\n  ⚠️  You can't afford this pet.")

def handle_sell_items(player: Player) -> None:
    """Handle selling items."""
    if player.location != Location.VILLAGE:
        print("\n  ⚠️  You can only sell items in the Village.")
        return
    
    sellable_items = [item for item in player.inventory if item in SELLABLE_ITEMS]
    
    if not sellable_items:
        print("\n  ⚠️  You have nothing to sell.")
        return
    
    print("\n" + "-"*40)
    print("  What would you like to sell?")
    print("-"*40 + "\n")
    
    for i, item in enumerate(sellable_items, 1):
        print(f"  {i}. {item:<20} ({SELLABLE_ITEMS[item]} gold)")
    print(f"\n  {len(sellable_items) + 1}. Cancel")
    
    options = [str(i) for i in range(1, len(sellable_items) + 2)]
    choice = get_valid_choice(options, "Choice:")
    
    choice_num = int(choice)
    if choice_num == len(sellable_items) + 1:
        print("\n  ✗ Cancelled.")
        return
    
    item = sellable_items[choice_num - 1]
    player.remove_item(item)
    player.add_gold(SELLABLE_ITEMS[item])
    print(f"\n  ✓ Sold {item} for {SELLABLE_ITEMS[item]} gold!")
    print("-"*40)

# ==================== QUEST FUNCTIONS ====================
def handle_quests(player: Player) -> None:
    """Handle quest management."""
    display_quests(player)
    
    print("\n  1. Start a new quest")
    print("  2. Abandon a quest")
    print("  3. Back to menu")
    
    choice = get_valid_choice(["1", "2", "3"], "Choice:")
    
    if choice == "1":
        available_quests = {qid: q for qid, q in QUESTS.items() 
                          if qid not in player.active_quests and 
                          qid not in player.completed_quests}
        if not available_quests:
            print("\n  ⚠️  No available quests.")
            return
        
        print("\n" + "-"*40)
        for i, (qid, quest) in enumerate(available_quests.items(), 1):
            print(f"  {i}. {quest['name']} - {quest['description']}")
        
        options = [str(i) for i in range(1, len(available_quests) + 1)]
        quest_choice = get_valid_choice(options, "Choice:")
        
        quest_id = list(available_quests.keys())[int(quest_choice) - 1]
        player.active_quests[quest_id] = 0
        print(f"\n  ✓ Started quest: {QUESTS[quest_id]['name']}")
        print("-"*40)
    
    elif choice == "2":
        if not player.active_quests:
            print("\n  ⚠️  No active quests to abandon.")
            return
        
        print("\n" + "-"*40)
        for i, qid in enumerate(player.active_quests.keys(), 1):
            quest = QUESTS[qid]
            print(f"  {i}. {quest['name']}")
        
        options = [str(i) for i in range(1, len(player.active_quests) + 1)]
        abandon_choice = get_valid_choice(options, "Choice:")
        
        quest_id = list(player.active_quests.keys())[int(abandon_choice) - 1]
        del player.active_quests[quest_id]
        print(f"\n  ✓ Abandoned quest: {QUESTS[quest_id]['name']}")
        print("-"*40)

def check_quest_completion(player: Player, quest_id: str) -> bool:
    """Check if a quest is completed."""
    if quest_id not in player.active_quests:
        return False
    
    quest = QUESTS[quest_id]
    progress = player.active_quests[quest_id]
    
    if progress >= quest["count"]:
        player.active_quests.pop(quest_id)
        player.completed_quests.append(quest_id)
        player.add_gold(quest["reward_gold"])
        player.gain_xp(quest["reward_xp"])
        
        print("\n" + "🎯"*20)
        print(f"\n  QUEST COMPLETE: {quest['name']}!")
        print(f"  Rewards: {quest['reward_gold']} gold, {quest['reward_xp']} XP")
        print("\n" + "🎯"*20 + "\n")
        
        return True
    
    return False

# ==================== CRAFTING FUNCTIONS ====================
def handle_crafting(player: Player) -> None:
    """Handle crafting."""
    display_crafting_menu(player)
    
    available_recipes = [recipe for recipe_name, recipe in CRAFTING_RECIPES.items() 
                        if recipe.get("level", 1) <= player.level]
    
    if not available_recipes:
        return
    
    options = [str(i) for i in range(1, len(available_recipes) + 2)]
    choice = get_valid_choice(options, "Choice:")
    
    if int(choice) == len(available_recipes) + 1:
        return
    
    recipe = available_recipes[int(choice) - 1]
    
    # Check ingredients
    has_all_ingredients = True
    for ingredient, needed_count in recipe["ingredients"].items():
        if player.inventory.count(ingredient) < needed_count:
            has_all_ingredients = False
            print(f"\n  ⚠️  You need {needed_count} {ingredient}(s) but only have {player.inventory.count(ingredient)}")
    
    if not has_all_ingredients:
        return
    
    # Remove ingredients
    for ingredient, needed_count in recipe["ingredients"].items():
        for _ in range(needed_count):
            player.remove_item(ingredient)
    
    # Add crafted item
    result = recipe["result"]
    player.add_item(result)
    
    if result not in player.crafted_items:
        player.crafted_items[result] = 0
    player.crafted_items[result] += 1
    
    print(f"\n  ✓ You crafted {result}!")
    print(f"    Value: {recipe['price']} gold")

# ==================== BATTLE SYSTEM ====================
def calculate_player_damage(player: Player) -> Tuple[int, bool, Optional[str]]:
    """Calculate damage dealt by player. Returns (damage, is_critical, enchantment)."""
    base_damage = random.randint(player.offense, player.offense + 10)
    
    # Critical hit chance based on level
    critical_chance = 0.05 + (player.level * 0.01)
    is_critical = random.random() < critical_chance
    
    # Check for enchanted weapons
    enchantment = None
    for weapon, ench in player.enchanted_items.items():
        if weapon in player.inventory:
            if ench == "Fire":
                base_damage += random.randint(3, 6)
                enchantment = "fire"
            elif ench == "Poison":
                if random.random() < 0.2:
                    base_damage += random.randint(2, 5)
                    enchantment = "poison"
            elif ench == "Critical":
                critical_chance += 0.15
                is_critical = random.random() < critical_chance
            break
    
    if is_critical:
        base_damage = int(base_damage * 1.5)
    
    return base_damage, is_critical, enchantment

def calculate_enemy_damage(enemy: Enemy) -> int:
    """Calculate damage dealt by enemy."""
    min_dmg, max_dmg = enemy.damage_range
    return random.randint(min_dmg, max_dmg)

def get_random_treasure() -> str:
    """Get a random treasure item."""
    if random.random() < 0.1:  # 10% chance of cursed item
        return random.choice(CURSED_TREASURES)
    return random.choice(TREASURES)

def get_battle_reward(player: Player, enemy: Enemy) -> int:
    """Get random gold reward from battle."""
    base_reward = random.randint(10, 30)
    if enemy.is_boss:
        base_reward *= 3
    return base_reward

def apply_dodge(player: Player) -> bool:
    """Check if player dodges an attack."""
    return random.random() < player.dodge

def get_mystery_box() -> Dict:
    """Get a random mystery box reward."""
    rarity = random.choices(["common", "uncommon", "rare", "legendary"], 
                           weights=[60, 25, 10, 5])[0]
    
    rewards = {
        "common": {"gold": random.randint(20, 50), "item": random.choice(["Small Potion", "Dagger"])},
        "uncommon": {"gold": random.randint(50, 100), "item": random.choice(["Medium Potion", "Sword", "Shield"])},
        "rare": {"gold": random.randint(100, 200), "item": random.choice(["Large Potion", "Axe", "Boots"])},
        "legendary": {"gold": random.randint(200, 500), "item": "Legendary Sword"},
    }
    
    return rewards[rarity]

def fight_enemy(player: Player, enemy: Enemy) -> bool:
    """
    Battle an enemy.
    
    Args:
        player: The player
        enemy: The enemy to fight
    
    Returns:
        True if player won, False if player fled
    """
    display_battle_start(enemy, player.time_of_day)
    
    pet_helper = player.pet if player.pet and random.random() < 0.5 else None
    if pet_helper:
        print(f"\n  🐾 {player.pet.pet_type} joins the battle!")
    
    while enemy.is_alive() and player.health > 0:
        action = get_valid_choice(["attack", "run"], "Attack or Run?").lower()
        
        if action == "attack":
            damage, is_critical, enchantment = calculate_player_damage(player)
            
            # Pet attacks too
            if pet_helper:
                pet_damage = pet_helper.get_damage()
                damage += pet_damage
                print(f"  🐾 {player.pet.pet_type} deals {pet_damage} damage!")
            
            enemy.take_damage(damage)
            player.total_damage_dealt += damage
            display_damage_dealt(damage, is_critical, enchantment)
            print(f"    {enemy.name} Health: {max(enemy.health, 0)}")
            
            if not enemy.is_alive():
                # Enemy defeated
                gold_reward = get_battle_reward(player, enemy)
                treasure = get_random_treasure()
                player.add_gold(gold_reward)
                
                # Mystery box chance
                if random.random() < 0.15:
                    mystery_box = get_mystery_box()
                    player.add_gold(mystery_box["gold"])
                    player.add_item(mystery_box["item"])
                    player.mystery_boxes_opened += 1
                    print(f"\n  📦 MYSTERY BOX! You found {mystery_box['item']} and {mystery_box['gold']} gold!")
                
                # Check for cursed items
                if treasure in CURSED_TREASURES:
                    player.add_item(treasure)
                    display_curse_warning(treasure)
                    player.add_status_effect(StatusEffect.POISON, 5)
                else:
                    player.add_item(treasure)
                    player.update_treasure_quest()
                
                display_enemy_defeated(enemy, gold_reward, treasure)
                player.gain_xp(enemy.xp)
                player.battles_won += 1
                
                if enemy.name not in player.enemies_defeated:
                    player.enemies_defeated[enemy.name] = 0
                player.enemies_defeated[enemy.name] += 1
                player.update_quest_progress(enemy.name)
                player.add_to_bestiary(enemy.name, enemy)
                
                drop = ANIMAL_DROPS.get(enemy.name)
                if drop:
                    player.add_item(drop)
                    display_enemy_drop(enemy, drop)
                
                # Add value to sellable items if they're treasures
                if treasure in TREASURES:
                    if treasure not in SELLABLE_ITEMS:
                        SELLABLE_ITEMS[treasure] = random.randint(30, 80)
                
                # Check quest completion
                for quest_id in list(player.active_quests.keys()):
                    check_quest_completion(player, quest_id)
                
                # Check achievements
                player.check_achievements()
                
                print("\n" + "="*40)
                return True
            
            # Enemy counterattack - check dodge first
            if apply_dodge(player):
                print(f"\n  ⚡ You dodged the {enemy.name}'s attack!")
            else:
                enemy_damage = calculate_enemy_damage(enemy)
                
                # Pet takes some damage
                if pet_helper and random.random() < 0.3:
                    pet_damage_taken = random.randint(3, 8)
                    pet_helper.take_damage(pet_damage_taken)
                    if not pet_helper.is_alive():
                        print(f"\n  💔 {player.pet.pet_type} fainted!")
                        pet_helper = None
                    else:
                        print(f"\n  💔 {player.pet.pet_type} takes {pet_damage_taken} damage!")
                
                player.take_damage(enemy_damage)
                display_damage_taken(enemy, enemy_damage, player.health)
                
                # Enemy special abilities
                if enemy.is_boss and random.random() < 0.3:
                    ability = random.choice(enemy.abilities)
                    print(f"\n  💥 {enemy.name} uses {ability}!")
                    if "Heal" in ability:
                        enemy.heal(20)
                        print(f"    {enemy.name} healed to {enemy.health}")
                    elif "Poison" in ability:
                        player.add_status_effect(StatusEffect.POISON, 3)
                        print(f"    You are poisoned!")
                    elif "Drain" in ability:
                        player.take_damage(10)
                        enemy.heal(10)
                
                # Apply status effects
                player.apply_status_effects()
        
        elif action == "run":
            display_ran_away(enemy)
            return False
    
    if player.health <= 0:
        display_game_over("You were defeated...")
        player.battles_lost += 1
        if player.hardcore_mode:
            raise SystemExit
        return False
    
    return False

def fight_final_boss(player: Player) -> None:
    """
    Battle the final boss.
    
    Args:
        player: The player
    """
    boss = Enemy(FINAL_BOSS_DATA["name"], FINAL_BOSS_DATA["health"], 
                 FINAL_BOSS_DATA["damage_range"], FINAL_BOSS_DATA["xp"], True)
    
    print(f"\n  {boss.name} Health: {boss.health}\n")
    print("█"*40)
    
    pet_helper = player.pet if player.pet else None
    if pet_helper:
        print(f"\n  🐾 {player.pet.pet_type} joins the final battle!")
    
    while boss.is_alive() and player.health > 0:
        action = get_valid_choice(["attack", "run"], "Attack or Run?").lower()
        
        if action == "attack":
            damage, is_critical, enchantment = calculate_player_damage(player)
            
            if pet_helper:
                pet_damage = pet_helper.get_damage()
                damage += pet_damage
                print(f"  🐾 {player.pet.pet_type} deals {pet_damage} damage!")
            
            boss.take_damage(damage)
            player.total_damage_dealt += damage
            display_damage_dealt(damage, is_critical, enchantment)
            print(f"    {boss.name} Health: {max(boss.health, 0)}")
            
            if not boss.is_alive():
                display_victory()
                player.gain_xp(boss.xp)
                player.battles_won += 1
                player.check_achievements()
                raise SystemExit
            
            # Boss counterattack
            if apply_dodge(player):
                print(f"\n  ⚡ You dodged the {boss.name}'s attack!")
            else:
                boss_damage = calculate_enemy_damage(boss)
                
                if pet_helper and random.random() < 0.2:
                    pet_damage_taken = random.randint(5, 10)
                    pet_helper.take_damage(pet_damage_taken)
                    if not pet_helper.is_alive():
                        print(f"\n  💔 {player.pet.pet_type} fainted!")
                        pet_helper = None
                    else:
                        print(f"\n  💔 {player.pet.pet_type} takes {pet_damage_taken} damage!")
                
                player.take_damage(boss_damage)
                print(f"\n  ⚡ The {boss.name} strikes you for {boss_damage} damage!")
                print(f"    Your health: {player.health} / {player.max_health}")
                
                # Boss special abilities
                if random.random() < 0.4:
                    ability = random.choice(boss.abilities)
                    print(f"\n  💥 Shadow Lord uses {ability}!")
                    if "Dark Aura" in ability:
                        player.add_status_effect(StatusEffect.BURN, 2)
        
        elif action == "run":
            display_cannot_escape()
    
    if player.health <= 0:
        display_game_over(f"The {boss.name} has defeated you...")
        player.battles_lost += 1
        raise SystemExit

# ==================== TRAVEL SYSTEM ====================
def handle_travel(player: Player) -> None:
    """Handle player travel to a new location."""
    location_choice = get_location_choice(player)
    
    if location_choice is None:
        return
    
    player.location = location_choice
    player.travel()
    print(f"\n  🛤️  You travel to the {player.location.value}...")
    print("-"*40)
    
    # Random encounters
    if player.location != Location.VILLAGE and random.random() < 0.3:
        print("\n  ⚠️  Random encounter!")
        
        # Use night enemies if it's night
        if player.time_of_day == TimeOfDay.NIGHT and player.location in NIGHT_ENEMIES:
            enemy_data = random.choice(NIGHT_ENEMIES[player.location])
        elif player.location in ENEMY_DATA:
            enemy_data = random.choice(ENEMY_DATA[player.location])
        else:
            enemy_data = None
        
        if enemy_data:
            enemy = Enemy(
                enemy_data["name"],
                int(enemy_data["health"] * DIFFICULTY_MULTIPLIERS[player.difficulty]["health"]),
                tuple(int(x * DIFFICULTY_MULTIPLIERS[player.difficulty]["damage"]) 
                      for x in enemy_data["damage_range"]),
                enemy_data["xp"],
                enemy_data["boss"]
            )
            fight_enemy(player, enemy)
    
    if player.travel_count >= TRAVELS_TO_FINAL_BOSS:
        display_final_boss_arrival()
        fight_final_boss(player)
    else:
        display_travel_info(player)
        
        # Regular enemy encounter
        if player.location in ENEMY_DATA and random.random() < 0.6:
            # Use night enemies if it's night
            if player.time_of_day == TimeOfDay.NIGHT and player.location in NIGHT_ENEMIES:
                enemy_data = random.choice(NIGHT_ENEMIES[player.location])
            else:
                enemy_data = random.choice(ENEMY_DATA[player.location])
            
            enemy = Enemy(
                enemy_data["name"],
                int(enemy_data["health"] * DIFFICULTY_MULTIPLIERS[player.difficulty]["health"]),
                tuple(int(x * DIFFICULTY_MULTIPLIERS[player.difficulty]["damage"]) 
                      for x in enemy_data["damage_range"]),
                enemy_data["xp"],
                enemy_data["boss"]
            )
            fight_enemy(player, enemy)

# ==================== MAIN GAME LOOP ====================
def main() -> None:
    """Main game loop."""
    print("\n" + "★"*40)
    print("     TEXT ADVENTURE GAME")
    print("★"*40)
    
    player_name = input("\n  Enter your name: ").strip().title()
    
    # Difficulty selection
    print("\n" + "="*40)
    print("  Select Difficulty:")
    print("="*40)
    print("\n  1. Easy (70% enemy stats, 150% gold)")
    print("  2. Normal (100% enemy stats, 100% gold)")
    print("  3. Hard (130% enemy stats, 80% gold)")
    print("\n" + "="*40)
    
    diff_choice = get_valid_choice(["1", "2", "3"], "Choice:")
    
    difficulty_map = {"1": Difficulty.EASY, "2": Difficulty.NORMAL, "3": Difficulty.HARD}
    difficulty = difficulty_map[diff_choice]
    
    player = Player(player_name, difficulty)
    
    print(f"\n  Welcome, {player.name}!")
    print("  Your adventure begins...\n")
    
    # Skill tree selection
    display_skill_tree_selection()
    skill_choice = get_valid_choice(["1", "2", "3"], "Choice:")
    
    skill_map = {"1": "warrior", "2": "rogue", "3": "paladin"}
    player.choose_skill_tree(skill_map[skill_choice])
    print(f"\n  ✓ You chose the {player.skill_tree.capitalize()} path!")
    
    print("★"*40 + "\n")
    
    # Start with tutorial quest
    player.active_quests["wolf_slayer"] = 0
    
    while True:
        display_menu()
        choice = get_valid_choice([item.value for item in MenuItem])
        
        if choice == MenuItem.TRAVEL.value:
            handle_travel(player)
            player.apply_skill_bonuses()
        elif choice == MenuItem.SHOP.value:
            handle_shop(player)
        elif choice == MenuItem.STATS.value:
            display_player_stats(player)
        elif choice == MenuItem.INVENTORY.value:
            display_inventory(player)
        elif choice == MenuItem.SELL.value:
            handle_sell_items(player)
        elif choice == MenuItem.QUESTS.value:
            handle_quests(player)
        elif choice == MenuItem.MAP.value:
            display_map(player)
        elif choice == MenuItem.PETS.value:
            display_pets(player)
            if player.pet:
                pet_choice = get_valid_choice(["1", "2"], "Choice:")
                if pet_choice == "1":
                    player.pet = None
                    print("\n  ✗ Your pet has left you.")
        elif choice == MenuItem.CRAFTING.value:
            handle_crafting(player)
        elif choice == MenuItem.ACHIEVEMENTS.value:
            display_achievements(player)
        elif choice == MenuItem.BESTIARY.value:
            display_bestiary(player)
        elif choice == MenuItem.QUIT.value:
            print("\n  Thanks for playing!\n")
            break
        
        # Check win condition
        if "Magic Ring" in player.inventory and player.location == Location.CASTLE:
            print("\n" + "★"*40)
            print("     YOU WIN!")
            print("★"*40)
            print("\n  You obtained the Magic Ring!")
            print("  The castle is secured!")
            print(f"\n  Final Stats:")
            print(f"    • Level: {player.level}")
            print(f"    • Battles Won: {player.battles_won}")
            print(f"    • Total Damage: {player.total_damage_dealt}")
            print(f"    • Enemies Defeated: {sum(player.enemies_defeated.values())}")
            print(f"    • Gold: {player.gold}")
            print(f"    • Achievements: {sum(1 for ach in ACHIEVEMENTS.values() if ach['unlocked'])} / {len(ACHIEVEMENTS)}")
            print(f"    • Treasures: {player.treasures_collected}")
            print(f"    • Mystery Boxes: {player.mystery_boxes_opened}")
            print("\n" + "★"*40 + "\n")
            break

if __name__ == "__main__":
    main()