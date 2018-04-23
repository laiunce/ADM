--campos twitter

text
user.created_at
user.name
user.screen_name
user.followers_count
user.following
user.friends_count
user.location
user.profile_image_url
retweet_count
retweeted_status.extended_tweet.full_text
retweeted_status.user.created_at
retweeted_status.user.name
retweeted_status.user.screen_name
retweeted_status.user.followers_count
retweeted_status.user.following
retweeted_status.user.friends_count
retweeted_status.user.location
retweeted_status.user.profile_image_url
retweeted_status.retweet_count


--columnas importantes
GET /twitter/bajada_twitter/_search
{
  "query": { "match_all": {} },
  "_source": ["text","user.created_at","user.name","user.screen_name","user.followers_count","user.following","user.friends_count","user.location","user.profile_image_url","retweet_count","retweeted_status.extended_tweet.full_text","retweeted_status.user.created_at","retweeted_status.user.name","retweeted_status.user.screen_name","retweeted_status.user.followers_count","retweeted_status.user.following","retweeted_status.user.friends_count","retweeted_status.user.location","retweeted_status.user.profile_image_url","retweeted_status.retweet_count"]
}




GET /twitter/bajada_twitter/_search
{
  "query": { "match_all": {} },
  "_source": ["user.screen_name","user.followers_count"]
}



GET /twitter/bajada_twitter/_search
{
  "query": { "match_all": {} },
  "_source": ["user.screen_name","user.followers_count"]
}






GET /twitter/bajada_twitter/_search
{
  "size": 0,
  "aggregations": {
    "total_per_year": {
      "terms": {
        "field": "user.screen_name"
      }
    },
    "total_per_price": {
      "terms": {
        "field": "user.followers_count"
      }
    }
  }
}






curl -XGET 'http://localhost:9200/authors/famousbooks/_search?&pretty=true&size=3' -d {
  "size": 0,
  "aggs": {
    "authors-aggs": {
      "terms": {
        "field": "Author"
      }
    }
  }
}


curl -X PUT "http://localhost:9200/authors1/famousbooks/_mapping" -d {
  "famousbooks": {
    "properties": {
      "Author": {
        "type": "string",
        "index": "not_analyzed"
      }
    }
  }
}









PUT twitter/_mapping/bajada_twitter
{
  "properties": {
    "text": { 
      "type":     "text",
      "fielddata": true
    }
  }
}


GET /twitter/bajada_twitter/_search
{
  "size": 0,
  "aggs": {
    "authors-aggs": {
      "terms": {
        "field": "text"
      }
    }
  }
}









