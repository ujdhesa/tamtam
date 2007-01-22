
#ifndef MYFLT
# define MYFLT float
# define DEF_MYFLT
#endif

#ifdef __cplusplus
extern "C"
{
#endif
    void sc_destroy();
    int sc_initialize(char * csd);
    void sc_instrumentLoad(int, const char *);
    void sc_instrumentUnloadBatch(int);
    void sc_micRecord(int);
    void sc_setMasterVolume(double);
    void sc_scoreEvent15(char type, MYFLT p1, MYFLT p2, MYFLT p3, MYFLT p4, MYFLT p5, MYFLT p6, MYFLT p7, MYFLT p8, MYFLT p9, MYFLT p10, MYFLT p11, MYFLT p12, MYFLT p13, MYFLT p14, MYFLT p15);
    void sc_start();
    void sc_stop();

    void sc_loop_addScoreEvent15(char type, MYFLT p1, MYFLT p2, MYFLT p3, MYFLT p4, MYFLT p5, MYFLT p6, MYFLT p7, MYFLT p8, MYFLT p9, MYFLT p10, MYFLT p11, MYFLT p12, MYFLT p13, MYFLT p14, MYFLT p15);
    void sc_loop_clear();
    int sc_loop_getTick();
    void sc_loop_playing(int tf);
    void sc_loop_setNumTicks(int nticks);
    void sc_loop_setTick(int ctick);
    void sc_loop_setTickDuration(double secs_per_tick);
#ifdef __cplusplus
}
#endif

#ifdef DEF_MYFLT
# undef MYFLT
# undef DEF_MYFLT
#endif
