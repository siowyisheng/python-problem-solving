# separate into batches

### Task: Separate a list of elements, returning a 2d list with the inner lists having a specified length.

```
ls = [i for i in range(500)]
BATCH_SIZE = 128

2d_ls = []
while batch < len(ls) // BATCH_SIZE + 2:
    start = (batch - 1) * BATCH_SIZE
    end = batch * BATCH_SIZE
    2d_ls.append(ls[start:end])
    batch += 1
```
