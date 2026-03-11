import time

def retry_chain(chain, input_data, retries=3):

    for i in range(retries):

        try:

            result = chain.invoke(input_data)

            if result:
                return result

        except Exception as e:

            print("Retry:", i, e)

        time.sleep(3)

    raise Exception("Failed after retries")
