#!/usr/bin/env python3

# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   Travel_weather_planner.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mny-aro- <mny-aro-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/05 10:16:05 by mny-aro-            #+#    #+#            #
#   Updated: 2026/10/05 10:16:05 by mny-aro-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


distance_mi = 0
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

if not distance_mi:
    print(False)
elif distance_mi <= 1:
    print(not is_raining)
elif distance_mi <= 6:
    print(has_bike and not is_raining)
else:
    print(has_car or has_ride_share_app)
