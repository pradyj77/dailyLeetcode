class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        .  ==> current directory
        .. ==> previous/parent directory
        // or /// ==> '/'
        ... or .... or any other than above ==> valid directory



        Simplified ==>

        path must start with '/'
        directories within the path must be separated by '/'
        path must not end with '/' unless it's a root directory
        path must not have any single or double periods '.' or '..' 
         - used to denote current or parent directories


        Examples:

        "/home/" ==> "/home"
        "/home//foo/" ==> "/home/foo"
        "/home/user/Documents/../Pictures" ==> "/home/user/Pictures"
        "/../" ==> "/"
        "/.../a/../b/c/../d/./" ==> "/.../b/d"

        Questions?

        Can there be more than 2 or 3 slashes? Such as '//////' or '///'
        Can the input path not start with '/'?

        O(n)

        Let's get all the consecutive slashes together and then replace those 
        - with single slash starting from longest slash to smallest
        
        Check if path starts with '/'? if not add it
        Check if last '/' is ther? If yes, get rid of it
        Once replaced, let's split the string with '/'
        if there are any single periods - get rid of those from the array
        if there are double periods - get rid of that along with parent
        '''

        # index = 0
        # slashes = {}
        # path = path.replace('/./', '/')

        # while index < len(path):
        #     if path[index] == '/':
        #         curr = ""
        #         while index < len(path) and path[index] == '/':
        #             curr += '/'
        #             index += 1
        #         slashes[len(curr)] = curr
        #     else:
        #         index += 1

        # #print(slashes)
        # sorted_slashes = sorted(slashes.keys(), reverse=True)
        

        # for item in sorted_slashes:
        #     #print("LOL", slashes[item])
        #     path = path.replace(slashes[item], '/')

        # if path[0] != '/':
        #     path = '/' + path
        
        # path = path.replace('/./', '/')

        # #print(path)

        # pathArr = path.split('/')
        
        # print(pathArr)

        # resultPath = "/"
        # skipPositions = {}

        # index = 0

        # while index < len(pathArr):
        #     if pathArr[index] == '..':
        #         counter = 0
        #         start = 0
        #         while index < len(pathArr) and pathArr[index] == '..':
        #             counter += 1
        #             start = index
        #             index += 1
        #         # print("index", index)
        #         # print("counter", counter)
        #         counter = 2 * counter
        #         while counter > 0:
        #             skipPositions[start] = True
        #             start -= 1
        #             counter -= 1
        #     else:
        #         index += 1

        # print(skipPositions)
        
        # for i in range(0, len(pathArr)):
        #     if pathArr[i] == '':
        #         continue
        #     if pathArr[i] != '.' and i not in skipPositions:
        #         if i != len(pathArr) - 1:
        #             resultPath = resultPath + pathArr[i] + '/'
        #         else:
        #             resultPath = resultPath + pathArr[i]
        
        # #print(resultPath)
        # if resultPath[-1] == '/':
        #     resultPath = resultPath[:-1]

        # if resultPath == '':
        #     return '/'
        # #print(resultPath)
        # return resultPath


        stack = []

        for item in path.split('/'):
            if item == '..':
                if stack:
                    stack.pop()
            elif item == '.' or not item:
                continue
            else:
                stack.append(item)

        return "/" + "/".join(stack)