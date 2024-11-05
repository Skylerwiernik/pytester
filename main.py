from robot import Ava
import asyncio
async def main():
    ava = Ava()
    while True:
        ava.motor1.speed.value = 0.5
        ava.motor2.speed.value = -0.5
        await asyncio.sleep(1)
        ava.motor1.speed.value = -0.5
        ava.motor2.speed.value = 0.5
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
