import eel
from models.player import Player
from models.quest import Quest
from models.shop import Shop
from models.skill import Skill


def main():
    eel.init('gui', allowed_extensions=['.js', '.html'])
    eel.start('index.html', size=(480, 480))


if __name__ == '__main__':
    main()
