from prefect.infrastructure import Process

process_block = Process(env={"PREFECT_LOGGING_LEVEL": "INFO"})
process_block.save("prod", overwrite=True)
