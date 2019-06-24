Title: Bulk redirection with Nginx
Slug: bulk-redirect-with-nginx
Date: 2017-09-25 16:43
Tags: devops, nginx
Category: software
featured_image: https://images.unsplash.com/photo-1463267738627-d1a780134be7?dpr=1&auto=compress,format&fit=crop&w=1000&h=&q=80&cs=tinysrgb&crop=
Summary: Walkthrough of how you can utilize the power of nginx to setup mass redirects of random urls on your server


In this post, I am going to talk about how you can setup a redirects on a server for many individual paths. It uses the hash map

## Creating files

Create a file called `redirects-map.conf`, each line of the file will represents a redirect rule. The format of line is:

```
<old_location> <new_url>;
```

`old_location` can be specified in both regex or plan simple path.

The regex version looks likes this:
```
~^/showcase/(.*)?$ /projects/;
```
The plan simple location redirect will look like:
```
/contact-success/ /contact;
```

So your `redirects-map.conf` file should look like:

```nginx
# /etc/nginx/redirects-map.conf 

/contact-success/ /contact;
~^/showcase/(.*)?$ /projects/;
```

## Setting up nginx

1. Upload the `redirects-map.conf` to your server at `/etc/nginx`
2. Add the following at the top of your nginx virtualhost file, which imports the file and creates a hash map:

```nginx
map $uri $redirected_url {
    default "none";
    include /etc/nginx/redirects-map.conf;
}
```

Then in the `server` block, write the following rule:

```nginx
# pre-defined redirects
if ($redirected_url != "none") {
    rewrite ^ $redirected_url permanent;
}
```

Now your virtualhost conf file should look like:

```nginx
map $uri $redirected_url {
    default "none";
    include /etc/nginx/redirects-map.conf;
}

server {
    listen        443 ssl http2;
    server_name   example.org;

    # pre-defined redirects
    if ($redirected_url != "none") {
        rewrite ^ $redirected_url permanent;
    }

    # rest of the rules

}
```

!!!warning
    Nginx has a limit on how big the `redirects-map.conf` can be, which is controlled via `map_hash_bucket_size` variable. If you get the following error, `[emerg]: could not build the map_hash`, you should increase the `map_hash_bucket_size` to account for the filesize. Say your redirects-map.conf is 30Kb, you set the `map_hash_bucket_size` variable in the `http` block of `nginx.conf` to `30720`;
