# boot.dev asteroids game project
## Log
- 20250303 : Scoring system added, score shown in top left
- 20250304 : Game resets on death

## Tasklist
- [x] Add a scoring system
  - [x] Big meteors least points (5), mid meteors (10), small meteors (15)
  - [x] Store points inside asteroid instances
  - [x] On bullet-asteroid collision, add points to score
- [ ] Create screen overlay
  - [x] Show score in top left
- [ ] Implement multiple lives and respawning
  - [ ] Health bar + a few i-frames is a bit more forgiving; can be combined with lives and respawning
  - [ ] i-frames make the ship blink for a second or 2
  - [ ] Health bar is an RGBA color fill of the ship (alpha increases when being damaged?)
  - [ ] Bigger meteors do more damage to health
  - [ ] On collision with ship, meteors should bounce in another direction
  - [ ] Animation around the ship when colliding (squiggly lines)
- [ ] Add alternative controls
  - [ ] rotate with mouse
  - [ ] strafe with left-right buttons
- [ ] Add an explosion effect for the asteroids
- [ ] Add acceleration to the player movement
  - [ ] Speed from stand-still accelerates slow
  - [ ] Momentum keeps the ship moving in a direction for some time, need to counter to slow down faster
- [ ] Make the objects wrap around the screen instead of disappearing
  - [ ] For this mode, set an asteroid amount limit, after which no new ones will spawn, except from meteor splits
- [ ] Add a background image
- [ ] Create different weapon types
- [ ] Make the asteroids lumpy instead of perfectly round
- [ ] Make the ship have a triangular hit box instead of a circular one
- [ ] Add a shield power-up
- [ ] Add a speed power-up
- [ ] Add bombs that can be dropped
- [ ] Add a dustcloud, that hurts the ship the longer you're inside
  - [ ] Shooting the dustcloud dillutes it, making it bigger in size but less damaging
  - [ ] When reaching a max diameter, the cloud disappears
  - [ ] The chance of a dust cloud appearing is dependant on the amount of asteroids destroyed
