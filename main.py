import requests, json, os

url = "https://replit.com/graphql"

headers = {
    "accept": "application/json; charset=utf-8",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "content-type": "application/json; charset=utf-8",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "origin": "https://replit.com",
    "referer": "https://replit.com/repls/folder/Archive/CC31A%3A%20USACO%20Silver%20Basic%20A",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
    "cookie": '''__stripe_mid=0499a761-2a5c-4baf-8c46-fea493f2c3102b1736; cf_clearance=30b58abae04c6ec1992c74d602235da500e896e5-1629129844-0-150; hubspotutk=61f4a1e92e3babc8952023b474af8450; __hssrc=1; _ga=GA1.2.1142902446.1648509807; ajs_user_id=196205; _anon_id=80a1defe-c469-456b-9741-f36d4329e127; connect.sid=s%3AnxTPECfenOzRKGHZKuKQmx6lF0AeP_gs.kn%2BO%2B4whSGrI4mgFjSkiYiLLIRmW8uT95TJlHy%2BfGBI; __hstc=205638156.61f4a1e92e3babc8952023b474af8450.1633810748592.1650208156552.1652571886968.16; replit:authed=1; replit_authed=1; _gid=GA1.2.591970461.1653753464; __stripe_sid=a4486bc8-9154-48c4-9c31-317e3436be1390665b; amplitudeSessionId=1653791389; ajs_anonymous_id=c5eaf6c1-13a0-4f7a-aaa5-45e7cf9393b0; replit_ng=1653792859.325.46.818813|8035451343a2d8f3e54599c71b2aec19; _dd_s=logs=1&id=49b1674e-7659-46c9-9833-a7b5026664fc&created=1653789336704&expire=1653793932445&rum=1''',
}

s = requests.Session()

try:
    os.mkdir('./Files')
except:
    pass

try:
    os.mkdir('./Replits')
except:
    pass


def get_files(path):
    if path != "":
        payload = '''[{"operationName":"ReplsDashboardReplFolderList","variables":{"path":"folder''' + path + '''"},"query":"query ReplsDashboardReplFolderList($path: String!, $starred: Boolean, $after: String) {\n  currentUser {\n    id\n    username\n    replFolderByPath(path: $path) {\n      id\n      ownerId: userId\n      pathnames\n      canEdit\n      canCreateSubFolders\n      parent {\n        id\n        pathnames\n        __typename\n      }\n      folders {\n        id\n        ...ReplsDashboardFolderItemReplFolder\n        __typename\n      }\n      repls(starred: $starred, after: $after) {\n        items {\n          id\n          ...ReplsDashboardReplItemRepl\n          __typename\n        }\n        pageInfo {\n          nextCursor\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ReplsDashboardFolderItemReplFolder on ReplFolder {\n  id\n  name\n  canEdit\n  pathnames\n  image\n  timeCreated\n  replsCount\n  folderType\n  __typename\n}\n\nfragment ReplsDashboardReplItemRepl on Repl {\n  id\n  title\n  description\n  timeCreated\n  size\n  isStarred\n  isPrivate\n  isOwner\n  isAlwaysOn\n  isBoosted\n  slug\n  url\n  hostedUrl\n  templateInfo {\n    label\n    __typename\n  }\n  ...ReplsDashboardReplItemActionsRepl\n  ...ReplLinkRepl\n  user {\n    id\n    image\n    username\n    ...UserLinkUser\n    __typename\n  }\n  config {\n    isServer\n    __typename\n  }\n  isRenamed\n  __typename\n}\n\nfragment ReplsDashboardReplItemActionsRepl on Repl {\n  id\n  slug\n  historyUrl\n  pinnedToProfile\n  isPrivate\n  currentUserPermissions {\n    changeTitle\n    changeDescription\n    changeLanguage\n    changeConfig\n    changePrivacy\n    star\n    pin\n    move\n    delete\n    leaveMultiplayer\n    viewHistory\n    fork\n    __typename\n  }\n  __typename\n}\n\nfragment ReplLinkRepl on Repl {\n  id\n  url\n  nextPagePathname\n  __typename\n}\n\nfragment UserLinkUser on User {\n  id\n  url\n  username\n  __typename\n}\n"},{"operationName":"CurriculumHubLaunchModal","variables":{},"query":"query CurriculumHubLaunchModal {\n  currentUser {\n    id\n    isTeacher: hasRole(role: TEACHER)\n    teamOrganizations(subscriptionType: EDUCATION) {\n      id\n      teams {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"},{"operationName":"TourServiceToursSeen","variables":{"tours":["privacy-update-09/21","learn-onboarding","profile-refresh-beta","curriculum-launch-modal","projects-overview-cta","stack-create-cta","stack-migration-cta","youtube-in-the-ws","cleanup-popover-dismissed","add-guest-new-user","repl-talk-update-2021","repl-talk-update-2022","search","profile2"]},"query":"query TourServiceToursSeen($tours: [String!]!) {\n  currentUser {\n    id\n    toursSeen(tours: $tours) {\n      id\n      ...TourServiceTour\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment TourServiceTour on TourSeen {\n  id\n  seen\n  __typename\n}\n"}]'''
    else:
        payload = '''[{"operationName":"ReplsDashboardReplFolderList","variables":{"path":""},"query":"query ReplsDashboardReplFolderList($path: String!, $starred: Boolean, $after: String) {\n  currentUser {\n    id\n    username\n    replFolderByPath(path: $path) {\n      id\n      ownerId: userId\n      pathnames\n      canEdit\n      canCreateSubFolders\n      parent {\n        id\n        pathnames\n        __typename\n      }\n      folders {\n        id\n        ...ReplsDashboardFolderItemReplFolder\n        __typename\n      }\n      repls(starred: $starred, after: $after) {\n        items {\n          id\n          ...ReplsDashboardReplItemRepl\n          __typename\n        }\n        pageInfo {\n          nextCursor\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ReplsDashboardFolderItemReplFolder on ReplFolder {\n  id\n  name\n  canEdit\n  pathnames\n  image\n  timeCreated\n  replsCount\n  folderType\n  __typename\n}\n\nfragment ReplsDashboardReplItemRepl on Repl {\n  id\n  title\n  description\n  timeCreated\n  size\n  isStarred\n  isPrivate\n  isOwner\n  isAlwaysOn\n  isBoosted\n  slug\n  url\n  hostedUrl\n  templateInfo {\n    label\n    __typename\n  }\n  ...ReplsDashboardReplItemActionsRepl\n  ...ReplLinkRepl\n  user {\n    id\n    image\n    username\n    ...UserLinkUser\n    __typename\n  }\n  config {\n    isServer\n    __typename\n  }\n  isRenamed\n  __typename\n}\n\nfragment ReplsDashboardReplItemActionsRepl on Repl {\n  id\n  slug\n  historyUrl\n  pinnedToProfile\n  isPrivate\n  currentUserPermissions {\n    changeTitle\n    changeDescription\n    changeLanguage\n    changeConfig\n    changePrivacy\n    star\n    pin\n    move\n    delete\n    leaveMultiplayer\n    viewHistory\n    fork\n    __typename\n  }\n  __typename\n}\n\nfragment ReplLinkRepl on Repl {\n  id\n  url\n  nextPagePathname\n  __typename\n}\n\nfragment UserLinkUser on User {\n  id\n  url\n  username\n  __typename\n}\n"},{"operationName":"CurriculumHubLaunchModal","variables":{},"query":"query CurriculumHubLaunchModal {\n  currentUser {\n    id\n    isTeacher: hasRole(role: TEACHER)\n    teamOrganizations(subscriptionType: EDUCATION) {\n      id\n      teams {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"},{"operationName":"TourServiceToursSeen","variables":{"tours":["privacy-update-09/21","learn-onboarding","profile-refresh-beta","curriculum-launch-modal","projects-overview-cta","stack-create-cta","stack-migration-cta","youtube-in-the-ws","cleanup-popover-dismissed","add-guest-new-user","repl-talk-update-2021","repl-talk-update-2022","search","profile2"]},"query":"query TourServiceToursSeen($tours: [String!]!) {\n  currentUser {\n    id\n    toursSeen(tours: $tours) {\n      id\n      ...TourServiceTour\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment TourServiceTour on TourSeen {\n  id\n  seen\n  __typename\n}\n"}]'''

    r = s.post(url=url, headers=headers, json=json.loads(payload.replace("\n", "")))
    arr = r.json()
    print(path)
    print(r.status_code)

    folders = arr[0]['data']['currentUser']['replFolderByPath']['folders']
    repls = arr[0]['data']['currentUser']['replFolderByPath']['repls']['items']

    for folder in folders:
        folder_name = folder['name'].replace(' ', '-')
        if folder_name == "Multiplayer-repls":
            continue

        try:
            os.mkdir('./Files' + path.replace(' ', '-') + '/' + folder_name)
        except:
            pass

        try:
            os.mkdir('./Replits' + path.replace(' ', '-') + '/' + folder_name)
        except:
            pass

        print(path + '/' + folder['name'])
        get_files(path + '/' + folder['name'])

    for repl in repls:
        download_link = "https://replit.com" + repl['url'] + ".zip"
        repl_name = repl['title'].replace(' ', '-')

        r = s.get(url=download_link, headers=headers)
        print(r.status_code)

        f = open("./Files" + path.replace(' ', '-') + '/' + repl_name + ".zip", "wb+")
        f.write(r.content)


def get_multiplayer_files():
    payload = '''[{"operationName":"ReplsDashboardReplFolderList","variables":{"path":"multiplayer"},"query":"query ReplsDashboardReplFolderList($path: String!, $starred: Boolean, $after: String) {\n  currentUser {\n    id\n    username\n    replFolderByPath(path: $path) {\n      id\n      ownerId: userId\n      pathnames\n      canEdit\n      canCreateSubFolders\n      parent {\n        id\n        pathnames\n        __typename\n      }\n      folders {\n        id\n        ...ReplsDashboardFolderItemReplFolder\n        __typename\n      }\n      repls(starred: $starred, after: $after) {\n        items {\n          id\n          ...ReplsDashboardReplItemRepl\n          __typename\n        }\n        pageInfo {\n          nextCursor\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ReplsDashboardFolderItemReplFolder on ReplFolder {\n  id\n  name\n  canEdit\n  pathnames\n  image\n  timeCreated\n  replsCount\n  folderType\n  __typename\n}\n\nfragment ReplsDashboardReplItemRepl on Repl {\n  id\n  title\n  description\n  timeCreated\n  size\n  isStarred\n  isPrivate\n  isOwner\n  isAlwaysOn\n  isBoosted\n  slug\n  url\n  hostedUrl\n  templateInfo {\n    label\n    __typename\n  }\n  ...ReplsDashboardReplItemActionsRepl\n  ...ReplLinkRepl\n  user {\n    id\n    image\n    username\n    ...UserLinkUser\n    __typename\n  }\n  config {\n    isServer\n    __typename\n  }\n  isRenamed\n  __typename\n}\n\nfragment ReplsDashboardReplItemActionsRepl on Repl {\n  id\n  slug\n  historyUrl\n  pinnedToProfile\n  isPrivate\n  currentUserPermissions {\n    changeTitle\n    changeDescription\n    changeLanguage\n    changeConfig\n    changePrivacy\n    star\n    pin\n    move\n    delete\n    leaveMultiplayer\n    viewHistory\n    fork\n    __typename\n  }\n  __typename\n}\n\nfragment ReplLinkRepl on Repl {\n  id\n  url\n  nextPagePathname\n  __typename\n}\n\nfragment UserLinkUser on User {\n  id\n  url\n  username\n  __typename\n}\n"},{"operationName":"CurriculumHubLaunchModal","variables":{},"query":"query CurriculumHubLaunchModal {\n  currentUser {\n    id\n    isTeacher: hasRole(role: TEACHER)\n    teamOrganizations(subscriptionType: EDUCATION) {\n      id\n      teams {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"},{"operationName":"TourServiceToursSeen","variables":{"tours":["privacy-update-09/21","learn-onboarding","profile-refresh-beta","curriculum-launch-modal","projects-overview-cta","stack-create-cta","stack-migration-cta","youtube-in-the-ws","cleanup-popover-dismissed","add-guest-new-user","repl-talk-update-2021","repl-talk-update-2022","search","profile2"]},"query":"query TourServiceToursSeen($tours: [String!]!) {\n  currentUser {\n    id\n    toursSeen(tours: $tours) {\n      id\n      ...TourServiceTour\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment TourServiceTour on TourSeen {\n  id\n  seen\n  __typename\n}\n"}]'''

    try:
        os.mkdir('./Files/Multiplayer')
    except:
        pass

    try:
        os.mkdir('./Replits/Multiplayer')
    except:
        pass

    r = s.post(url=url, headers=headers, json=json.loads(payload.replace("\n", "")))
    arr = r.json()
    repls = arr[0]['data']['currentUser']['replFolderByPath']['repls']['items']

    for repl in repls:
        download_link = "https://replit.com" + repl['url'] + ".zip"
        repl_name = repl['title'].replace(' ', '-')

        r = s.get(url=download_link, headers=headers)
        #print(repl_name, r.status_code)

        f = open("./Files/Multiplayer/" + repl_name + ".zip", "wb+")
        f.write(r.content)


get_files("")
#get_multiplayer_files()