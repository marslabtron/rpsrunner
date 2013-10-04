Rock Paper Scissors Runner
=====================

I just stole the runner from http://www.rpscontest.com/
Then added Grunt to handle testing of bots.

# Installation

npm install

# Finding Bots

Visit http://www.rpscontest.com/leaderboard

# Usage

1. Bring your fighters into the fight via symlink.

   ```
   cd fighting_ring
   ln -s ../bots/momo_bot.py momo_bot.py
   ```

2. run ```grunt watch```

3. Edit bots in bots/ folder, watch them fight.
