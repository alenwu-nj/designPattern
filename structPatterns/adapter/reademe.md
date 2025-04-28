例如刚开始的时候，我们只使用了mysql, 后来可能使用其他的db, 例如postgresql，
在封装我们的sdk的时候，用户并不希望看到db的具体实现，只需要知道我们提供的接口即可，
所以我们需要一个适配层，将db的具体实现隐藏起来，只暴露我们提供的接口。

我们可以定义一个接口，比如DbAdapter，然后在这个接口中定义所有db操作的方法，
然后在具体的实现类中实现这些方法，比如MysqlDbAdapter，PostgresqlDbAdapter。

然后在我们的sdk中，只需要依赖DbAdapter这个接口，然后在初始化的时候，
通过配置文件或者其他方式，选择具体的实现类，比如MysqlDbAdapter。
这样，我们的sdk就不需要知道具体的db实现，只需要依赖DbAdapter这个接口，
然后调用DbAdapter的方法即可。