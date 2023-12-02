import time

first = True # 첫 번째 쓰레드 생성 여부를 확인하기 위한 플래그

async def create_thread_message(ai_client, thread_id, assistant_id, content):
    # 주어진 내용으로 새로운 쓰레드 메시지를 생성하고 실행(run)
    thread_message = ai_client.beta.threads.messages.create(
        thread_id,
        role="user",
        content=content,
    )
    run = ai_client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )
    return run.id

async def check_run_status(ai_client, thread_id, run_id):
    # 실행(run)의 상태를 확인하는 함수
    start_time = time.time()
    while time.time() - start_time < 30:  # 30초 시간 초과 시 탈출
        run = ai_client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id
        )
        if run.status == "completed": # 실행이 완료된 경우
            return "completed", run
        elif run.status in ["failed", "cancelled"]: # 실행이 실패하거나 취소된 경우
            return run.status, None
        time.sleep(2)
    return "timeout", None # 30초가 지나면 타임아웃 처리

async def initialize_thread(ai_client, thread_id):
    global first
    print(first) # token.txt 안에 있는 쓰레드를 삭제하지 않기 위해서
    if first != True:
        response = ai_client.beta.threads.delete(thread_id)
    empty_thread = ai_client.beta.threads.create() # 빈 쓰레드 생성
    first = False
    print(first)
    return empty_thread.id

async def recreate_assistant(client, ai_client, assistant_id):
    # OpenAI Assistant를 재생성하는 함수
    client.beta.assistants.delete(assistant_id) # 현재 어시스턴트 삭제
    my_assistant = ai_client.beta.assistants.create(
        instructions="You are a discord bot. When asked a question, answer like a game-loving friend.",
        name="GameBuddyBot",
        model="gpt-3.5-turbo-1106",
    )
    return my_assistant.id