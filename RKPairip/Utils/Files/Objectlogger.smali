.class public LRK_TECHNO_INDIA/ObjectLogger;
.super Ljava/lang/Thread;
# static fields
.field private static final PARAMETER_BUFFER:Ljava/lang/ThreadLocal;
.field private static final QUEUE:Ljava/util/concurrent/LinkedBlockingQueue;
.field private static final TIME_FORMAT1:Ljava/text/SimpleDateFormat;
.field private static final TIME_FORMAT2:Ljava/text/SimpleDateFormat;
# direct methods
.method static constructor <clinit>()V
    .registers 2
    new-instance v0, Ljava/text/SimpleDateFormat;
    const-string v1, "HH:mm:ss.SSS"
    invoke-direct {v0, v1}, Ljava/text/SimpleDateFormat;-><init>(Ljava/lang/String;)V
    sput-object v0, LRK_TECHNO_INDIA/ObjectLogger;->TIME_FORMAT1:Ljava/text/SimpleDateFormat;
    new-instance v0, Ljava/text/SimpleDateFormat;
    const-string v1, "yyyyMMddHHmmssSSS"
    invoke-direct {v0, v1}, Ljava/text/SimpleDateFormat;-><init>(Ljava/lang/String;)V
    sput-object v0, LRK_TECHNO_INDIA/ObjectLogger;->TIME_FORMAT2:Ljava/text/SimpleDateFormat;
    new-instance v0, Ljava/util/concurrent/LinkedBlockingQueue;
    invoke-direct {v0}, Ljava/util/concurrent/LinkedBlockingQueue;-><init>()V
    sput-object v0, LRK_TECHNO_INDIA/ObjectLogger;->QUEUE:Ljava/util/concurrent/LinkedBlockingQueue;
    new-instance v0, Ljava/lang/ThreadLocal;
    invoke-direct {v0}, Ljava/lang/ThreadLocal;-><init>()V
    sput-object v0, LRK_TECHNO_INDIA/ObjectLogger;->PARAMETER_BUFFER:Ljava/lang/ThreadLocal;
    new-instance v0, LRK_TECHNO_INDIA/ObjectLogger;
    invoke-direct {v0}, LRK_TECHNO_INDIA/ObjectLogger;-><init>()V
    const/4 v1, 0x1
    invoke-virtual {v0, v1}, LRK_TECHNO_INDIA/ObjectLogger;->setDaemon(Z)V
    invoke-virtual {v0}, LRK_TECHNO_INDIA/ObjectLogger;->start()V
    return-void
.end method
.method public constructor <init>()V
    .registers 1
    invoke-direct {p0}, Ljava/lang/Thread;-><init>()V
    return-void
.end method
.method public static logstring(Ljava/lang/Object;)V
    .registers 9
    invoke-static {p0}, LRK_TECHNO_INDIA/ObjectLogger;->y(Ljava/lang/Object;)Ljava/lang/String;
    move-result-object v0
    invoke-static {v0}, LRK_TECHNO_INDIA/ObjectLogger;->EscapeStrings(Ljava/lang/String;)Ljava/lang/String;
    move-result-object v0
    invoke-static {v0}, LRK_TECHNO_INDIA/ObjectLogger;->z(Ljava/lang/String;)V
    return-void
.end method
.method public static EscapeStrings(Ljava/lang/String;)Ljava/lang/String;
    .registers 4
    const-string v0, "\\"
    const-string v1, "\\\\"
    invoke-virtual {p0, v0, v1}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v0
    const-string v1, "\t"
    const-string v2, "\\t"
    invoke-virtual {v0, v1, v2}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v0
    const-string v1, "\b"
    const-string v2, "\\b"
    invoke-virtual {v0, v1, v2}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v0
    const-string v1, "\n"
    const-string v2, "\\n"
    invoke-virtual {v0, v1, v2}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v0
    const-string v1, "\r"
    const-string v2, "\\r"
    invoke-virtual {v0, v1, v2}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v0
    const-string v1, "\f"
    const-string v2, "\\f"
    invoke-virtual {v0, v1, v2}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v0
    const-string v1, "\'"
    const-string v2, "\\\'"
    invoke-virtual {v0, v1, v2}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v0
    const-string v1, "\""
    const-string v2, "\\\""
    invoke-virtual {v0, v1, v2}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v0
    return-object v0
.end method
.method private static y(Ljava/lang/Object;)Ljava/lang/String;
    .registers 3
    if-nez p0, :cond_5
    const-string v0, "null"
    return-object v0
    :cond_5
    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;
    move-result-object v0
    invoke-virtual {v0}, Ljava/lang/Class;->isArray()Z
    move-result v1
    if-eqz v1, :cond_77
    const-class v1, [B
    if-ne v0, v1, :cond_1b
    move-object v1, p0
    check-cast v1, [B
    invoke-static {v1}, Ljava/util/Arrays;->toString([B)Ljava/lang/String;
    move-result-object v1
    return-object v1
    :cond_1b
    const-class v1, [S
    if-ne v0, v1, :cond_27
    move-object v1, p0
    check-cast v1, [S
    invoke-static {v1}, Ljava/util/Arrays;->toString([S)Ljava/lang/String;
    move-result-object v1
    return-object v1
    :cond_27
    const-class v1, [I
    if-ne v0, v1, :cond_33
    move-object v1, p0
    check-cast v1, [I
    invoke-static {v1}, Ljava/util/Arrays;->toString([I)Ljava/lang/String;
    move-result-object v1
    return-object v1
    :cond_33
    const-class v1, [J
    if-ne v0, v1, :cond_3f
    move-object v1, p0
    check-cast v1, [J
    invoke-static {v1}, Ljava/util/Arrays;->toString([J)Ljava/lang/String;
    move-result-object v1
    return-object v1
    :cond_3f
    const-class v1, [C
    if-ne v0, v1, :cond_4b
    move-object v1, p0
    check-cast v1, [C
    invoke-static {v1}, Ljava/util/Arrays;->toString([C)Ljava/lang/String;
    move-result-object v1
    return-object v1
    :cond_4b
    const-class v1, [F
    if-ne v0, v1, :cond_57
    move-object v1, p0
    check-cast v1, [F
    invoke-static {v1}, Ljava/util/Arrays;->toString([F)Ljava/lang/String;
    move-result-object v1
    return-object v1
    :cond_57
    const-class v1, [D
    if-ne v0, v1, :cond_63
    move-object v1, p0
    check-cast v1, [D
    invoke-static {v1}, Ljava/util/Arrays;->toString([D)Ljava/lang/String;
    move-result-object v1
    return-object v1
    :cond_63
    const-class v1, [Z
    if-ne v0, v1, :cond_6f
    move-object v1, p0
    check-cast v1, [Z
    invoke-static {v1}, Ljava/util/Arrays;->toString([Z)Ljava/lang/String;
    move-result-object v1
    return-object v1
    :cond_6f
    move-object v1, p0
    check-cast v1, [Ljava/lang/Object;
    invoke-static {v1}, Ljava/util/Arrays;->deepToString([Ljava/lang/Object;)Ljava/lang/String;
    move-result-object v1
    return-object v1
    :cond_77
    invoke-virtual {p0}, Ljava/lang/Object;->toString()Ljava/lang/String;
    move-result-object v1
    return-object v1
.end method
.method private static z(Ljava/lang/String;)V
    .registers 8
    const-string v0, "{\n\"[LOCATION]\"\n\"[RESULT]\"\n}\n"
    const-string v1, "[TIME]"
    invoke-virtual {v0, v1}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z
    move-result v2
    if-eqz v2, :cond_1c
    sget-object v2, LRK_TECHNO_INDIA/ObjectLogger;->TIME_FORMAT1:Ljava/text/SimpleDateFormat;
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J
    move-result-wide v3
    invoke-static {v3, v4}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;
    move-result-object v3
    invoke-virtual {v2, v3}, Ljava/text/SimpleDateFormat;->format(Ljava/lang/Object;)Ljava/lang/String;
    move-result-object v2
    invoke-virtual {v0, v1, v2}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v0
    :cond_1c
    new-instance v1, Ljava/lang/Throwable;
    invoke-direct {v1}, Ljava/lang/Throwable;-><init>()V
    invoke-virtual {v1}, Ljava/lang/Throwable;->getStackTrace()[Ljava/lang/StackTraceElement;
    move-result-object v1
    const/4 v2, 0x2
    aget-object v1, v1, v2
    invoke-virtual {v1}, Ljava/lang/StackTraceElement;->getFileName()Ljava/lang/String;
    move-result-object v2
    if-nez v2, :cond_30
    const-string v2, "Unknown Source"
    :cond_30
    invoke-virtual {v1}, Ljava/lang/StackTraceElement;->getLineNumber()I
    move-result v3
    if-ltz v3, :cond_4a
    new-instance v4, Ljava/lang/StringBuilder;
    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V
    invoke-virtual {v4, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    const-string v5, ":"
    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;
    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v2
    :cond_4a
    const-string v4, "[RESULT]"
    invoke-virtual {v0, v4, p0}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v4
    invoke-virtual {v1}, Ljava/lang/StackTraceElement;->getClassName()Ljava/lang/String;
    move-result-object v5
    const-string v6, "[CLASS]"
    invoke-virtual {v4, v6, v5}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v4
    invoke-virtual {v1}, Ljava/lang/StackTraceElement;->getMethodName()Ljava/lang/String;
    move-result-object v5
    const-string v6, "[METHOD]"
    invoke-virtual {v4, v6, v5}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v4
    const-string v5, "[LOCATION]"
    invoke-virtual {v4, v5, v2}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v0
    sget-object v4, LRK_TECHNO_INDIA/ObjectLogger;->QUEUE:Ljava/util/concurrent/LinkedBlockingQueue;
    invoke-virtual {v4, v0}, Ljava/util/concurrent/LinkedBlockingQueue;->offer(Ljava/lang/Object;)Z
    return-void
.end method
# virtual methods
.method public run()V
    .registers 10
    const/4 v0, 0x0
    const-string v1, "[SDCARD]/MT2/dictionary/[PACKAGE]-[TIME].mtd"
    invoke-static {}, Landroid/os/Environment;->getExternalStorageDirectory()Ljava/io/File;
    move-result-object v2
    invoke-virtual {v2}, Ljava/io/File;->getPath()Ljava/lang/String;
    move-result-object v2
    const-string v3, "[SDCARD]"
    invoke-virtual {v1, v3, v2}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v1
    const-string v2, "[PACKAGE]"
    const-string v3, "PACKAGENAME"
    invoke-virtual {v1, v2, v3}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v1
    sget-object v2, LRK_TECHNO_INDIA/ObjectLogger;->TIME_FORMAT2:Ljava/text/SimpleDateFormat;
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J
    move-result-wide v3
    invoke-static {v3, v4}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;
    move-result-object v3
    invoke-virtual {v2, v3}, Ljava/text/SimpleDateFormat;->format(Ljava/lang/Object;)Ljava/lang/String;
    move-result-object v2
    const-string v3, "[TIME]"
    invoke-virtual {v1, v3, v2}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v1
    const/16 v2, 0x5c
    const/16 v3, 0x2f
    invoke-virtual {v1, v2, v3}, Ljava/lang/String;->replace(CC)Ljava/lang/String;
    move-result-object v2
    const-string v3, "//"
    const-string v4, "/"
    invoke-virtual {v2, v3, v4}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v1
    const/4 v2, 0x0
    :try_start_3e
    new-instance v3, Ljava/io/File;
    invoke-direct {v3, v1}, Ljava/io/File;-><init>(Ljava/lang/String;)V
    invoke-virtual {v3}, Ljava/io/File;->getParentFile()Ljava/io/File;
    move-result-object v4
    if-eqz v4, :cond_4c
    invoke-virtual {v4}, Ljava/io/File;->mkdirs()Z
    :cond_4c
    new-instance v5, Ljava/io/FileOutputStream;
    const/4 v6, 0x1
    invoke-direct {v5, v3, v6}, Ljava/io/FileOutputStream;-><init>(Ljava/io/File;Z)V
    :try_end_52
    .catch Ljava/io/IOException; {:try_start_3e .. :try_end_52} :catch_54
    move-object v0, v5
    goto :goto_59
    :catch_54
    move-exception v3
    invoke-virtual {v3}, Ljava/io/IOException;->printStackTrace()V
    move-object v2, v3
    :goto_59
    if-nez v0, :cond_90
    :try_start_5b
    new-instance v3, Ljava/io/File;
    const-string v4, "/data/data/PACKAGENAME/dictionary"
    invoke-direct {v3, v4}, Ljava/io/File;-><init>(Ljava/lang/String;)V
    new-instance v4, Ljava/io/File;
    new-instance v5, Ljava/lang/StringBuilder;
    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V
    const-string v6, "PACKAGENAME-"
    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    sget-object v6, LRK_TECHNO_INDIA/ObjectLogger;->TIME_FORMAT2:Ljava/text/SimpleDateFormat;
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J
    move-result-wide v7
    invoke-static {v7, v8}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;
    move-result-object v7
    invoke-virtual {v6, v7}, Ljava/text/SimpleDateFormat;->format(Ljava/lang/Object;)Ljava/lang/String;
    move-result-object v6
    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    const-string v6, ".mtd"
    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v5
    invoke-direct {v4, v3, v5}, Ljava/io/File;-><init>(Ljava/io/File;Ljava/lang/String;)V
    invoke-virtual {v3}, Ljava/io/File;->mkdirs()Z
    new-instance v5, Ljava/io/FileOutputStream;
    invoke-direct {v5, v4}, Ljava/io/FileOutputStream;-><init>(Ljava/io/File;)V
    :try_end_8e
    .catch Ljava/io/IOException; {:try_start_5b .. :try_end_8e} :catch_90
    move-object v0, v5
    goto :goto_90
    :catch_90
    :cond_90
    :goto_90
    :try_start_90
    invoke-static {}, Ljava/nio/charset/Charset;->defaultCharset()Ljava/nio/charset/Charset;
    move-result-object v3
    :goto_94
    sget-object v4, LRK_TECHNO_INDIA/ObjectLogger;->QUEUE:Ljava/util/concurrent/LinkedBlockingQueue;
    invoke-virtual {v4}, Ljava/util/concurrent/LinkedBlockingQueue;->take()Ljava/lang/Object;
    move-result-object v5
    check-cast v5, Ljava/lang/String;
    invoke-virtual {v5, v3}, Ljava/lang/String;->getBytes(Ljava/nio/charset/Charset;)[B
    move-result-object v6
    invoke-virtual {v0, v6}, Ljava/io/FileOutputStream;->write([B)V
    invoke-virtual {v4}, Ljava/util/concurrent/LinkedBlockingQueue;->isEmpty()Z
    move-result v4
    if-eqz v4, :cond_ac
    invoke-virtual {v0}, Ljava/io/FileOutputStream;->flush()V
    :try_end_ac
    .catch Ljava/lang/Exception; {:try_start_90 .. :try_end_ac} :catch_ad
    :cond_ac
    goto :goto_94
    :catch_ad
    move-exception v3
    new-instance v4, Ljava/lang/RuntimeException;
    invoke-direct {v4, v3}, Ljava/lang/RuntimeException;-><init>(Ljava/lang/Throwable;)V
    throw v4
.end method
