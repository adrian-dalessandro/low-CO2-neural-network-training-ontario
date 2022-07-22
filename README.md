
__Note__: Currently specific to Ontario
# Scheduler for Lowering CO2 Emissions Burden During Neural Network Optimization
Optimizing large neural networks on large datasets can be an energy intensive task. Naively performing this task creates a CO2 emissions burden, which contributes to the on-going climate catastrophe currently threatening human existence. However, many regions have governing bodies that provide two important measures which can aid in scheduling your neural network optimization workload:

1. Available supply from each generator source in MW
2. Current demand in MW

From this, we can calculate two important measures for determining emissions burden:

1. Supply and Demand Gap: If supply > demand, then energy is being wasted due to mismatch
2. Energy mix Cleanliness: Different sources of energy are used at different times of day, so the emissions burden fluctuates during the day

### TODO
- [ ] Write scheduler
- [ ] Create profiler for ieso energy mix data
