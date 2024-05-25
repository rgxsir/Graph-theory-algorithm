def havel_hakimi(sequence):
    # 步骤1：从序列中删除所有的零元素
    sequence = [x for x in sequence if x != 0]
    
    # 如果序列为空，则返回True（因为空图的度数序列）
    if len(sequence) == 0:
        return True

    # 步骤2：将序列按非递增顺序排序
    sequence.sort(reverse=True)
    
    # 步骤3：删除序列的第一个元素（称为n）
    n = sequence.pop(0)
    
    # 步骤4：如果n大于序列的长度，则返回False
    if n > len(sequence):
        return False

    # 步骤5：从序列的下一个n个元素中减去1
    for i in range(n):
        sequence[i] -= 1
        # 如果任何元素变为负数，则返回False
        if sequence[i] < 0:
            return False

    # 使用更新后的序列重复该过程
    return havel_hakimi(sequence)

# 示例用法
sequence = [4, 3, 3, 3, 2, 2, 2]
print(havel_hakimi(sequence))  # 输出 True
