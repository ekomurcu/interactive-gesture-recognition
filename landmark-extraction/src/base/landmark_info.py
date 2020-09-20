# Get id of each person to open up video directories
def get_ids(df):
    return df['ID'].unique()


# Get landmark columns for each gestures.
# Convert ids ndarray to dict to handle each videos columns
def init_landmarks_dict(ids, gestures):
    ids_with_landmark_col = {}
    for each_id in ids:
        ids_with_landmark_col[each_id] = {}
        for video_name in gestures:
            ids_with_landmark_col[each_id][video_name] = {'landmark_cols': [], 'nof_landmarks': 0}
    return ids_with_landmark_col


def get_landmark_info(df):
    df_frame = df[df.columns[5:]]
    return df_frame[df_frame > 0].dropna(axis='columns').keys(), int(
        df_frame[df_frame > 0].dropna(axis='columns').keys().shape[0] / 2)


def get_landmarks_info(ids, gestures):
    ids_with_landmark_col = init_landmarks_dict(ids, gestures)
    for each_id in ids:
        for video_name in gestures:
            source = str(each_id) + "/" + video_name + ".webm"
            # Select frame one
            frame_no = 1
            induced_df = df[(df['ID'] == each_id) & (df['source'] == source) & (df['frame'] == frame_no)]
            ids_with_landmark_col[each_id][video_name]['landmark_cols'] = get_landmark_info(induced_df)[0]
            ids_with_landmark_col[each_id][video_name]['nof_landmarks'] = get_landmark_info(induced_df)[1]
    return ids_with_landmark_col


# Print nof landmarks for each id.
def print_nof_landmarks(ids, gestures):
    landmarks_info = get_landmarks_info(get_ids(df), gestures)
    for each_id in ids:
        print("The number of landmarks for user " + str(each_id) + " is inorder as: ")
        nof_landmarks = []
        for video_name in gestures:
            nof_landmarks.append(landmarks_info[each_id][video_name]['nof_landmarks'])
        print(nof_landmarks)
