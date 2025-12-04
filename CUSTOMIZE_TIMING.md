# ⚙️ Customizing Load Test Timing - Complete Guide

## 📍 **File Locations**

### **Option 1: Simple Configuration (Most Common)**
**File:** `locust.conf`  
**Full Path:** `d:\Load-test-using-python-locast\locust.conf`

### **Option 2: Advanced Ramp-Up Profiles**
**File:** `load_profiles.py`  
**Full Path:** `d:\Load-test-using-python-locast\config\load_profiles.py`

---

## 🎯 **Option 1: Simple Configuration (Recommended)**

### **File: `locust.conf`**

This is the **easiest way** to customize your load test parameters.

### **Current Settings:**
```ini
host=https://staging.amal.education
users=50                    # Total number of concurrent users
spawn-rate=5                # Users spawned per second (ramp-up rate)
run-time=3m                 # Total test duration
headless=true
html=reports/html_reports/report.html
csv=reports/json_reports/locust_report
```

### **Customization Examples:**

#### **Example 1: Faster Ramp-Up**
```ini
users=100
spawn-rate=20              # Spawn 20 users/second (faster ramp-up)
run-time=5m
```
- **Ramp-up time:** 100 users ÷ 20 users/sec = **5 seconds**
- **Steady state:** 4 minutes 55 seconds at 100 users

#### **Example 2: Slower Ramp-Up (Gradual Load)**
```ini
users=200
spawn-rate=2               # Spawn 2 users/second (slower ramp-up)
run-time=10m
```
- **Ramp-up time:** 200 users ÷ 2 users/sec = **100 seconds (1m 40s)**
- **Steady state:** 8 minutes 20 seconds at 200 users

#### **Example 3: Quick Spike Test**
```ini
users=500
spawn-rate=100             # Spawn 100 users/second (very fast!)
run-time=2m
```
- **Ramp-up time:** 500 users ÷ 100 users/sec = **5 seconds**
- **Steady state:** 1 minute 55 seconds at 500 users

#### **Example 4: Long Endurance Test**
```ini
users=50
spawn-rate=1               # Spawn 1 user/second (very gradual)
run-time=30m
```
- **Ramp-up time:** 50 users ÷ 1 user/sec = **50 seconds**
- **Steady state:** 29 minutes 10 seconds at 50 users

### **Time Format Options:**
```ini
run-time=30s               # 30 seconds
run-time=5m                # 5 minutes
run-time=2h                # 2 hours
run-time=300               # 300 seconds (no unit = seconds)
```

---

## 🚀 **Option 2: Advanced Ramp-Up Profiles**

### **File: `config/load_profiles.py`**

Use this for **complex load patterns** with multiple stages.

### **Current Profile (HeavyLoad):**
```python
stages = [
    {"duration": 60, "users": 50, "spawn_rate": 5},      # Stage 1: 0-60s
    {"duration": 120, "users": 100, "spawn_rate": 10},   # Stage 2: 60-120s
    {"duration": 180, "users": 200, "spawn_rate": 20},   # Stage 3: 120-180s
]
```

**What this does:**
- **0-60 seconds:** Ramp up to 50 users at 5 users/sec
- **60-120 seconds:** Ramp up to 100 users at 10 users/sec
- **120-180 seconds:** Ramp up to 200 users at 20 users/sec
- **After 180 seconds:** Test stops

### **Custom Profile Examples:**

#### **Example 1: Gradual Ramp-Up with Plateau**
```python
from locust import LoadTestShape

class GradualRampUp(LoadTestShape):
    """
    Gradual ramp-up to test sustained load
    """
    stages = [
        {"duration": 60, "users": 25, "spawn_rate": 1},    # Slow start
        {"duration": 180, "users": 50, "spawn_rate": 2},   # Ramp to 50
        {"duration": 480, "users": 50, "spawn_rate": 0},   # Hold at 50 for 5 min
        {"duration": 600, "users": 0, "spawn_rate": 5},    # Ramp down
    ]
    
    def tick(self):
        run_time = self.get_run_time()
        for stage in self.stages:
            if run_time < stage["duration"]:
                return (stage["users"], stage["spawn_rate"])
        return None
```

#### **Example 2: Spike Test Pattern**
```python
from locust import LoadTestShape

class SpikeTest(LoadTestShape):
    """
    Sudden spike to test system resilience
    """
    stages = [
        {"duration": 60, "users": 10, "spawn_rate": 1},    # Baseline
        {"duration": 120, "users": 500, "spawn_rate": 100}, # SPIKE!
        {"duration": 240, "users": 500, "spawn_rate": 0},  # Hold spike
        {"duration": 300, "users": 10, "spawn_rate": 50},  # Back to baseline
    ]
    
    def tick(self):
        run_time = self.get_run_time()
        for stage in self.stages:
            if run_time < stage["duration"]:
                return (stage["users"], stage["spawn_rate"])
        return None
```

#### **Example 3: Step Load Pattern**
```python
from locust import LoadTestShape

class StepLoad(LoadTestShape):
    """
    Step-wise load increase
    """
    stages = [
        {"duration": 120, "users": 50, "spawn_rate": 5},   # Step 1
        {"duration": 240, "users": 100, "spawn_rate": 5},  # Step 2
        {"duration": 360, "users": 150, "spawn_rate": 5},  # Step 3
        {"duration": 480, "users": 200, "spawn_rate": 5},  # Step 4
        {"duration": 600, "users": 250, "spawn_rate": 5},  # Step 5
    ]
    
    def tick(self):
        run_time = self.get_run_time()
        for stage in self.stages:
            if run_time < stage["duration"]:
                return (stage["users"], stage["spawn_rate"])
        return None
```

#### **Example 4: Wave Pattern (Up and Down)**
```python
from locust import LoadTestShape

class WaveLoad(LoadTestShape):
    """
    Wave pattern - load goes up and down
    """
    stages = [
        {"duration": 60, "users": 50, "spawn_rate": 5},    # Wave up
        {"duration": 120, "users": 10, "spawn_rate": 5},   # Wave down
        {"duration": 180, "users": 100, "spawn_rate": 10}, # Wave up higher
        {"duration": 240, "users": 10, "spawn_rate": 10},  # Wave down
        {"duration": 300, "users": 150, "spawn_rate": 15}, # Wave up highest
        {"duration": 360, "users": 0, "spawn_rate": 15},   # End
    ]
    
    def tick(self):
        run_time = self.get_run_time()
        for stage in self.stages:
            if run_time < stage["duration"]:
                return (stage["users"], stage["spawn_rate"])
        return None
```

---

## 🔧 **How to Use Load Profiles**

### **Step 1: Edit `config/load_profiles.py`**

Add your custom profile or modify the existing `HeavyLoad` class.

### **Step 2: Update `locustfile.py`**

Add this line at the end of your `locustfile.py`:

```python
# At the end of locustfile.py
from config.load_profiles import HeavyLoad  # or your custom class name
```

Then change the user class to inherit from your shape:

```python
class MultiAPIUser(HttpUser):
    # ... existing code ...
    pass

# Add this at the end
class LoadTestWithShape(HeavyLoad):
    pass
```

**OR** simpler approach - just run with the shape class name:

```bash
locust -f locustfile.py --config locust.conf --class-name HeavyLoad
```

---

## 📊 **Comparison: Simple vs Advanced**

| Feature | `locust.conf` | `load_profiles.py` |
|---------|---------------|-------------------|
| **Ease of use** | ⭐⭐⭐⭐⭐ Very Easy | ⭐⭐⭐ Moderate |
| **Ramp-up control** | Single rate | Multiple stages |
| **Load patterns** | Linear only | Any pattern |
| **Best for** | Most tests | Complex scenarios |
| **File location** | Root directory | `config/` folder |

---

## 🎯 **Recommended Settings by Test Type**

### **1. Smoke Test (Quick Validation)**
**File:** `locust.conf`
```ini
users=5
spawn-rate=1
run-time=1m
```

### **2. Load Test (Normal Traffic)**
**File:** `locust.conf`
```ini
users=50
spawn-rate=5
run-time=10m
```

### **3. Stress Test (Find Breaking Point)**
**File:** `config/load_profiles.py`
```python
stages = [
    {"duration": 60, "users": 50, "spawn_rate": 5},
    {"duration": 180, "users": 100, "spawn_rate": 10},
    {"duration": 360, "users": 200, "spawn_rate": 20},
    {"duration": 600, "users": 500, "spawn_rate": 50},
]
```

### **4. Spike Test (Sudden Traffic)**
**File:** `config/load_profiles.py`
```python
stages = [
    {"duration": 60, "users": 10, "spawn_rate": 1},
    {"duration": 120, "users": 500, "spawn_rate": 100},  # Spike!
    {"duration": 300, "users": 10, "spawn_rate": 50},
]
```

### **5. Endurance Test (Long Duration)**
**File:** `locust.conf`
```ini
users=50
spawn-rate=2
run-time=2h
```

---

## 🔍 **Understanding the Parameters**

### **`users`**
- Total number of concurrent virtual users
- Higher = more load on the system

### **`spawn-rate`**
- How many users to add per second
- **Higher spawn-rate** = faster ramp-up, more aggressive
- **Lower spawn-rate** = slower ramp-up, more gradual

### **`run-time`**
- Total duration of the test
- Format: `30s`, `5m`, `2h`, or just a number (seconds)

### **`duration` (in load profiles)**
- Cumulative time from test start
- Each stage's duration is the **total time** from start, not the stage length

---

## ✅ **Quick Edit Guide**

### **For Simple Changes:**
1. Open `locust.conf`
2. Edit `users`, `spawn-rate`, or `run-time`
3. Save file
4. Run `run_tests.bat`

### **For Complex Patterns:**
1. Open `config\load_profiles.py`
2. Modify the `stages` list
3. Save file
4. Update `locustfile.py` to use the profile (if needed)
5. Run test

---

## 📋 **Summary**

| What to Customize | File | Location |
|-------------------|------|----------|
| **Users count** | `locust.conf` | `d:\Load-test-using-python-locast\locust.conf` |
| **Spawn rate (ramp-up speed)** | `locust.conf` | `d:\Load-test-using-python-locast\locust.conf` |
| **Test duration** | `locust.conf` | `d:\Load-test-using-python-locast\locust.conf` |
| **Multi-stage ramp-up** | `load_profiles.py` | `d:\Load-test-using-python-locast\config\load_profiles.py` |
| **Complex load patterns** | `load_profiles.py` | `d:\Load-test-using-python-locast\config\load_profiles.py` |

---

## 🎉 **Quick Start**

**To change ramp-up time right now:**

1. Open: `d:\Load-test-using-python-locast\locust.conf`
2. Change line 3: `spawn-rate=5` to your desired rate
3. Save and run: `run_tests.bat`

**Done!** 🚀
