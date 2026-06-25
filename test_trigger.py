from app.scripts.trigger_engine import TriggerEngine


engine = TriggerEngine(
    "app/rules.json",
    "app/trigger_queue.json"
)


result = engine.process_debug(
    "reincarnation",
    "ты хуй"
)


print(result)