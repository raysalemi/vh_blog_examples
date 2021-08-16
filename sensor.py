import asyncio
import time
import random

class SensorReader():
    def __init__(self):
        self.samples = []

    async def data_from_sensor(self):
        wait = random.randint(0,3)
        time.sleep(wait)
        sample = random.randint(50,80)
        print("Sample:", sample)
        return sample

    async def gather_ten_samples(self):
        self.samples = []
        while len(self.samples) < 10:
            sample = await self.data_from_sensor()
            self.samples.append(sample)
    
sr = SensorReader()
asyncio.run(sr.gather_ten_samples())
print("Samples:", sr.samples)


