def memoize(func):
    """装饰器：缓存函数结果。相同的位置参数第二次调用时直接返回缓存，不重复计算。

    可假设所有位置参数都可哈希；忽略关键字参数。
    必须用 functools.wraps 保留元数据。
    """
    # TODO: 用字典做缓存实现 memoize
    raise NotImplementedError
