Rock Paper Scissors Runner
=====================

I just stole the runner from http://www.rpscontest.com/
Then added Grunt to handle testing of bots.

# Installation

npm install

# Finding Bots

Visit http://www.rpscontest.com/leaderboard

# Usage

Bring your fighters into the fight via symlink.

example:
    cd fighting_ring
    ln -s ../bots/momo_bot.py momo_bot.py

grunt watch

edit bots in bots/ folder, watch them fight.
