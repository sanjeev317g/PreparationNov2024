def ipc(func):
    def rtos():
        print("Eswar works for RTOS")
        result = func()
        print("Anvesh works for IPC")
        return result
    return rtos

@ipc
def fcc():
    print("Vamsi works for fcc")
    return fcc

fcc()