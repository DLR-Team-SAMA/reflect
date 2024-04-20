from os import listdir as ls
import os
from shutil import copyfile as cp

thr_tsk_fld = 'thor_tasks'
st_summ_fld = 'state_summary'
kf_data_fld = 'keyframe_dataset'
tasks = ls(thr_tsk_fld)

def summary_to_keyframes(summary_fn,target_fn):
    with open(summary_fn, 'r') as f:
        summary = f.read()
        summary = summary.strip()
    summary = summary.split('\n')
    keyframes = []
    s = ''
    for line in summary:
        print(line[:5],end=' - ')
        frame_no = 60*int(line[:2]) + int(line[3:5])
        print(frame_no)
        s+=f'{frame_no}\n'
    s = s.strip()

    f = open(target_fn,'w')
    f.write(s)
    f.close()

# summ_fn = 'state_summary/boilWater/boilWater-1/state_summary_L1.txt'
# summary_to_keyframes(summ_fn,'keyframe_dataset/keyframes.txt')


for task in tasks:
    task_fld = f'{thr_tsk_fld}/{task}'
    cases = ls(task_fld)
    print(cases)
    for case in cases:
        thr_case_fld = f'{task_fld}/{case}'
        summ_case_fld = f'{st_summ_fld}/{task}/{case}'
        trg_fld = f'{kf_data_fld}/{task}/{case}'
        if(not os.path.exists(trg_fld)):
            os.makedirs(trg_fld)
        l1_summ_fn = f'{summ_case_fld}/state_summary_L1.txt'
        l2_summ_fn = f'{summ_case_fld}/state_summary_L2.txt'
        l1_trg_fn = f'{trg_fld}/keyframes_event.txt'
        l2_trg_fn = f'{trg_fld}/keyframes_subgoal.txt'
        summary_to_keyframes(l1_summ_fn,l1_trg_fn)
        summary_to_keyframes(l2_summ_fn,l2_trg_fn)
        src_tsk_fn = f'{thr_case_fld}/task.json'
        trg_tsk_fn = f'{trg_fld}/task.json'
        cp(src_tsk_fn,trg_tsk_fn)
        src_vid_fn = f'{thr_case_fld}/original-video.mp4'
        trg_vid_fn = f'{trg_fld}/original-video.mp4'
        cp(src_vid_fn,trg_vid_fn)