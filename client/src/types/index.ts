export type User = {
    id: string
    username: string
    email: string
    picture?:string
}

export type Media = {
    id: string
    uid: string
    file?: string
    filename: string
    url?: string
    size?: string
    content_type: string
    last_modified?: string
    extension?: string
}