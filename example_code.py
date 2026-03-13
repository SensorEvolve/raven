import asyncio
from datetime import datetime
from dataclasses import dataclass


@dataclass
class ThemeShowcase:
    """Testing docstring colors and multi-line strings."""

    version: float = 2.0
    is_active: bool = True

    def __init__(self, name: str):
        self.name = f"Highlight_{name}"
        self._value = 0xABC123  # Testing hex constants

    async def run_demo(self, items: list) -> None:
        try:
            for item in items:
                if item > 50:
                    print(f"[{datetime.now()}] High value: {item}")
                else:
                    await asyncio.sleep(0.1)
        except Exception as e:
            print(f"Error in {self.name}: {e}")


# Main execution block
if __name__ == "__main__":
    demo = ThemeShowcase("Gemini")
    sample_data = [10, 25, 66, 99]
    asyncio.run(demo.run_demo(sample_data))
